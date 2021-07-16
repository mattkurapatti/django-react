from rest_framework import serializers
from .models import Movie, Keyword

class KeywordSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), many=True)

    class Meta:
        model = Keyword
        fields = ('id', 'word', 'movies')

class MovieSerializer(serializers.ModelSerializer):
    keyword_list = KeywordSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'match_reason', 'tagline', 'overview', 'vote_average', 'mov_url', 'keyword_list')
