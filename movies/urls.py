from django.urls import path, re_path
from . import views

urlpatterns = [
    # default path
    path('api/movie/', views.MovieList.as_view()),
    # path with title, keyword, and rating as parameters
    path('api/movie/<title>/<keyword>/<rating>/', views.MovieList.as_view())
]
