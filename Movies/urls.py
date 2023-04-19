from django.conf.urls.static import static
from django.conf import settings as confSettings
from MovieList import settings
from django.urls import path
from .views import MoviesInfo, MovieDetail, api_root

urlpatterns = [
    path('', api_root, name="main"),
    path('movies-list/', MoviesInfo.as_view(), name="movies-list"),
    path('moviesList/movie/<int:pk>/', MovieDetail.as_view(), name="movie-detail")
] + static(confSettings.MEDIA_URL, document_root=settings.MEDIA_ROOT)