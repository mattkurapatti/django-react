from rest_framework import serializers
from .models import Movie, Keyword

class KeywordSerializer(serializers.RelatedField):
    # movies = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), many=True)
    # movies = serializers.ListField(source="word")

    # def to_representation(self, value):
    #     return value.word
    def to_representation(self, value):
        return value.word

    class Meta:
        model = Keyword
        fields = ('id', 'word', 'movies')

class MovieSerializer(serializers.ModelSerializer):
    keywords = KeywordSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'match_reason', 'tagline', 'overview', 'vote_average', 'mov_url', 'keywords')
