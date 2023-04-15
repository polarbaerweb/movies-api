from django.db import models
from datetime import datetime

TODAY = datetime.today()


class MoviesData(models.Model):
    name = models.CharField(max_length=255, null=False, default="undecided")
    premier_date = models.DateField(TODAY.strftime("%d-%b-%Y"))
    genres = models.CharField(max_length=255, default="undecided", null=False)
    description = models.TextField(max_length=600, default="undecided", null=False)
    directors = models.CharField(max_length=255, default="undecided", null=False)
    writers = models.CharField(max_length=255, default="undecided", null=False)
    actors = models.TextField(max_length=600, default="undecided", null=False)
    rating = models.FloatField(default=0, null=False, max_length=10)
    duration = models.TimeField(TODAY.strftime("%H:%M:%S"))
    owner = models.ForeignKey(
        "auth.user", related_name="Movies", on_delete=models.CASCADE, null=True
    )

    class Meta:
        ordering = ["duration"]

    def __str__(self):
        return self.name
