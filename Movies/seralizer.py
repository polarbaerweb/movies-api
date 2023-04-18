from rest_framework import serializers
from .models import MoviesData


class MoviesList(serializers.ModelSerializer):
    class Meta:
        model = MoviesData
        fields = "__all__"
