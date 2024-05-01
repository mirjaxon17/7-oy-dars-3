from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()
    last_update = models.DateField(auto_now=True)
    create_update = models.DateField(auto_now_add=True)

class Albom(models.Model):
    title = models.CharField(max_length=50)
    cover = models.URLField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    last_update = models.DateField(auto_now=True)
    create_update = models.DateField(auto_now_add=True)

class Song(models.Model):
    title = models.CharField(max_length=100)
    songs = models.URLField()
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE, null=True)
    last_update = models.DateField(auto_now=True)
    create_update = models.DateField(auto_now_add=True)

