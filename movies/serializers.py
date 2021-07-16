from rest_framework import serializers
from .models import Movie, Keyword

# we set use RelatedField so that we can pass keywords as a list
class KeywordSerializer(serializers.RelatedField):
    # specify that the "value" to be displayed for our Keyword is the value field
    def to_representation(self, value):
        return value.word

    class Meta:
        model = Keyword
        fields = ('id', 'word', 'movies')

class MovieSerializer(serializers.ModelSerializer):
    # many=True specifies many-to-many relationship
    keywords = KeywordSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'match_reason', 'tagline', 'overview', 'vote_average', 'mov_url', 'keywords')
