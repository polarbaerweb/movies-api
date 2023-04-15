from django.urls import path
from .views import MoviesInfo, MovieDetail, api_root

urlpatterns = [
    path('', api_root, name="main"),
    path('movies-list/', MoviesInfo.as_view(), name="movies-list"),
    path('moviesList/movie/<int:pk>/', MovieDetail.as_view(), name="movie-detail")
]