from django.db import models


class movies_data(models.Model):
    name = models.CharField(max_length=255, default="None", null=False)
    genres = models.ManyToManyField('Movies.Genre', related_name='Movies')
    premier_date = models.DateField()
    description = models.TextField(max_length=600, default="undecided", null=True)
    directors = models.ManyToManyField('Movies.Person', related_name='directors_movies')
    writers = models.ManyToManyField('Movies.Person', related_name='writers_movies')
    actors = models.ManyToManyField('Movies.Person', related_name='actor_in')
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    duration = models.DurationField()
    owner = models.ForeignKey(
        "auth.user", related_name="Movies", on_delete=models.CASCADE,
        null=True
    )
    poster = models.ImageField(upload_to="images")

    class Meta:
        ordering = ["duration"]

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255, null=False, default="undecided")

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=255, null=False, default="undecided")
    date_of_birth = models.DateTimeField()
    countOfFilms = models.IntegerField()

    def __str__(self):
        return self.name

