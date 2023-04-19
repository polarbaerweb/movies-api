from django.contrib import admin
from .models import *


class MoviesSettings(admin.ModelAdmin):
    list_display = ("owner", "duration")


admin.site.register(movies_data, MoviesSettings)
admin.site.register(Genre)
admin.site.register(Person)
