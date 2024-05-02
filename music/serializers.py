from rest_framework import serializers
from .models import Albom, Artist, Song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'image', 'last_update')

class AlbomSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only = True)
    class Meta:
        model = Albom
        fields = ('title', 'cover', 'artist','last_update')

class SongSerializer(serializers.ModelSerializer):
    albom = AlbomSerializer(read_only = True)
    class Meta:
        model = Song
        fields = ('title', 'song', 'albom', 'last_update')

