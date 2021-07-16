from django.shortcuts import render
from .models import Movie, Keyword
from .serializers import MovieSerializer, KeywordSerializer
from rest_framework import generics, viewsets, serializers

import json, urllib3
from urllib.request import urlopen

# I had issues with the API giving invalid urls, so this helper method checks the validity of a url
# https://stackoverflow.com/questions/10543940/check-if-a-url-to-an-image-is-up-and-exists-in-python
def valid_url(url):
    image_formats = ("image/png", "image/jpeg", "image/gif")
    try:
        site = urlopen(url)
        meta = site.info()  # get header of the http request
        if meta["content-type"] in image_formats:  # check if the content-type is a image
            return True
    except Exception:
        return False

# Create your views here.
class KeywordList(serializers.ModelSerializer):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

class MovieList(generics.ListCreateAPIView):
    serializer_class = MovieSerializer

    # returns filtered queryset
    def get_queryset(self):
        queryset = Movie.objects.all()
        # get parameters from url
        title = self.request.query_params.get('title')
        keyword = self.request.query_params.get('keyword')
        rating = self.request.query_params.get('rating')
        # set match reasons to default (if there are no inputted filters, the reason will be a default match"
        queryset.update(match_reason="Default Result")

        if keyword is not None and keyword != "":
            # filter out queries that don't have at least one keyword
            # which contains our keyword (as a substring)
            queryset = queryset.filter(keywords__word__icontains=keyword)
            for mov in queryset:
                mov.match_reason = "Keywords "
                mov.save()

        if title is not None and title != "":
            # filter out queries which don't have a title that
            # contain our title parameter as a substring
            queryset = queryset.filter(title__icontains=title)
            for mov in queryset:
                # check if the match also had a keyword match so that formatting
                # is accurate when displayed on front-end
                if mov.match_reason == "Default Result":
                    mov.match_reason = "Title"
                else:
                    mov.match_reason += " & Title"
                mov.save()

        if rating is not None and rating != 0:
            try:
                rating = float(rating)
                if rating < 0.0 or rating > 10.0:
                    raise IndexError("Rating out of bounds (Must be between 0-10)")
                queryset = queryset.filter(vote_average__gte=rating)
            except ValueError:
                print("Invalid decimal inputted for rating, no rating filter applied")
            except IndexError:
                print("Rating out of bounds (Must be between 0-10), no rating filter applied")

        # Get top 5 results
        queryset = queryset.distinct()[:5]
        for movie in queryset:
            try:
                # call api to get image url with top 5 results
                key = "nLuRdJU7ilmshomzNmLM800CKr4jp1NnF9pjsnz4Jvx28fyBHA"
                search = movie.title + ' movie poster'
                search_url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI?" \
                             "pageNumber=1&q=" + search + "&rapidapi-key=" + key
                search_url = search_url.replace(' ', '%20')
                with urlopen(search_url) as url:
                    # load json from api
                    data = json.loads(url.read().decode())
                    index = 0
                    poster_url = data['value'][index]['url']
                    # find first valid image url from response
                    while not valid_url(poster_url):
                        print(index)
                        index += 1
                        poster_url = data['value'][index]['url']
                    print(poster_url)
                    movie.mov_url = poster_url
                    movie.save()
            except ValueError:
                print("Bad Json Response")
            except Exception as e:
                print(e)
                print("Could not get image url for " + movie.title)
                continue

        return queryset
