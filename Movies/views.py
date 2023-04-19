from rest_framework import generics
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . import seralizer
from .models import movies_data, Person
from rest_framework.viewsets import ModelViewSet
from rest_framework import renderers


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


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = seralizer.PersonCurrent

    @action(detail=True, renderer_classes=[renderers.TemplateHTMLRenderer], url_name="byid", url_path="byid")
    def byid(self, request, pk=None):
        person = self.get_object()
        response = Response(template_name="index.html", data={"data": person})
        return response
