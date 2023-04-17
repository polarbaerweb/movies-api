from django.db import models


class MoviesData(models.Model):
    genres = models.ManyToManyField('Movies.Genre', related_name='Movies')
    premier_date = models.DateField()
    description = models.TextField(max_length=600, default="undecided", null=False)
    directors = models.ManyToManyField('Movies.Directors', related_name='Movies')
    writers = models.ManyToManyField('Movies.Writers', related_name='Movies')
    actors = models.ManyToManyField('Movies.Actors', related_name='Movies')
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    duration = models.DurationField()
    owner = models.ForeignKey(
        "auth.user", related_name="Movies", on_delete=models.CASCADE, null=True
    )
    poster = models.ImageField()

    class Meta:
        ordering = ["duration"]

    def __str__(self):
        return self.owner


class Genre(models.Model):
    name = models.CharField(max_length=255, null=False, default="undecided")

    def __str__(self):
        return self.name


class Directors(models.Model):
    name = models.CharField(max_length=255, null=False, default="undecided")

    def __str__(self):
        return self.name


class Writers(models.Model):
    name = models.CharField(max_length=255, null=False, default="undecided")

    def __str__(self):
        return self.name


class Actors(models.Model):
    name = models.CharField(max_length=255, null=False, default="undecided")

    def __str__(self):
        return self.name
