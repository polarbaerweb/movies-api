from rest_framework import serializers
from .models import MoviesData


class MoviesList(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="movie-detail",
        read_only=True
    )
    class Meta:
        model = MoviesData
        fields = (
            "name",
            "premier_date",
            "genres",
            "description",
            "directors",
            "writers",
            "actors",
            "rating",
            "duration",
            'url'
        )
