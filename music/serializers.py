from rest_framework import serializers
from .models import Albom, Artist, Song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'image', 'last_update')

class AlbomSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Albom
        fields = ('title', 'cover', 'artist','last_update')

class SongSerializer(serializers.ModelSerializer):
    albom = AlbomSerializer()
    class Meta:
        model = Song
        fields = ('title', 'songs', 'albom', 'last_update')