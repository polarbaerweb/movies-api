from django.contrib import admin
from .models import MoviesData


class MoviesSettings(admin.ModelAdmin):
    list_display = ("owner", "duration")


admin.site.register(MoviesData, MoviesSettings)
