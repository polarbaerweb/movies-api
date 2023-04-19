from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . import seralizer
from .models import movies_data


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "movies": reverse("movies-list", request=request, format=format)
        }
    )


class MoviesInfo(generics.ListCreateAPIView):
    queryset = movies_data.objects.all()
    serializer_class = seralizer.MoviesList
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )


class MovieDetail(generics.RetrieveUpdateAPIView):
    queryset = movies_data.objects.all()
    serializer_class = seralizer.MoviesList
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )