from django.contrib import admin
from .models import Artist, Albom, Song

admin.site.register([Albom, Artist, Song])