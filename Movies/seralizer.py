from rest_framework import serializers
from .models import movies_data, Genre, Person


class MoviesList(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    actors = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    directors = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    writers = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")

    class Meta:
        model = movies_data
        fields = "__all__"


class PersonCurrent(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class Genres(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

