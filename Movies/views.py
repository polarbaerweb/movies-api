from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . import seralizer
from .models import MoviesData


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "movies": reverse("movies-list", request=request, format=format)
        }
    )


class MoviesInfo(generics.ListCreateAPIView):
    queryset = MoviesData.objects.all()
    serializer_class = seralizer.MoviesList
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )


class MovieDetail(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = "./movies.html"

    def get(self, *args, **kwargs):
        queryset = MoviesData.objects.get(id=kwargs["pk"])
        return Response({"movies_data": queryset})