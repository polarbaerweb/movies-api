from django.contrib import admin
from .models import *


class MoviesSettings(admin.ModelAdmin):
    list_display = ("owner", "duration")


admin.site.register(MoviesData, MoviesSettings)
admin.site.register(Genre)
admin.site.register(Writers)
admin.site.register(Actors)
admin.site.register(Directors)
