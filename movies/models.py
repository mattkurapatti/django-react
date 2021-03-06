from django.db import models


# Create your models here.

class Movie(models.Model):
    movie_id = models.BigIntegerField(default=-1)
    title = models.CharField(max_length=200)
    match_reason = models.CharField(max_length=50)
    tagline = models.CharField(max_length=500, default="None")
    overview = models.CharField(max_length=1500, default="None")
    vote_average = models.DecimalField(max_digits=3, decimal_places=1, default=-1.0)
    mov_url = models.CharField(max_length=500)

class Keyword(models.Model):
    word = models.CharField(max_length=50)
    # Many to Many field describes relationship where Model A can have relationships
    # with multiple of Model B and Model B can have relationships with multiple of Model A
    movies = models.ManyToManyField(Movie, related_name='keywords')
