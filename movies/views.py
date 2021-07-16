from django.shortcuts import render
from .models import Movie, Keyword
from .serializers import MovieSerializer, KeywordSerializer
from rest_framework import generics, viewsets, serializers

import urllib.request, json


# Create your views here.

class KeywordList(serializers.ModelSerializer):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

class MovieList(generics.ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        title = self.request.query_params.get('title')
        keyword = self.request.query_params.get('keyword')
        rating = self.request.query_params.get('rating')
        queryset.update(match_reason="Default Result")

        if keyword is not None and keyword != "":
            queryset = queryset.filter(keyword__word__icontains=keyword)
            for mov in queryset:
                mov.match_reason = "Keywords"
                mov.save()

        if title is not None and title != "":
            queryset = queryset.filter(title__icontains=title)
            for mov in queryset:
                mov.match_reason = "Title"
                mov.save()

        if rating is not None:
            try:
                rating = float(rating)
                if rating < 0.0 or rating > 10.0:
                    raise IndexError("Rating out of bounds (Must be between 0-10)")
                queryset = queryset.filter(vote_average__gte=rating)
            except ValueError:
                print("Invalid decimal inputted for rating, no rating filter applied")
            except IndexError:
                print("Rating out of bounds (Must be between 0-10), no rating filter applied")

        queryset = queryset[:5]
        for movie in queryset:
            for keyword in movie.keywords.all():
                print(keyword.word)
            try:
                key = "nLuRdJU7ilmshomzNmLM800CKr4jp1NnF9pjsnz4Jvx28fyBHA"
                search = movie.title + ' movie poster'
                search_url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI?" \
                             "pageNumber=1&pageSize=1&q=" + search + "&rapidapi-key=" + key
                search_url = search_url.replace(' ', '%20')
                with urllib.request.urlopen(search_url) as url:
                    data = json.loads(url.read().decode())
                    poster_url = data['value'][0]['url']
                    print(poster_url)
                    movie.mov_url = poster_url
                    movie.save()
            except ValueError:
                print("Bad Json Response")
            except Exception:
                print("Could not get image url for " + movie.title)
                continue

        #print(queryset)
        # for movie in set(queryset):
        #     print(movie.title)
        return queryset
