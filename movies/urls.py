from django.urls import path, re_path
from . import views

urlpatterns = [
    path('api/movie/', views.MovieList.as_view()),
    path('api/movie/<title>/<keyword>/<rating>/', views.MovieList.as_view())
]
