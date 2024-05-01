from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Albom, Song
from .serializers import ArtistSerializer, AlbomSerializer, SongSerializer


class LandingPageAPIView(APIView):
    def get(self, request):
        return Response(data={"get api": "Hi lazy developers!"})
        
    def post(self, request):
        return Response(data={"post api": "this is post request api"})
    
class ArtistAPIView(APIView):
    def get(self, request):
        artist = Artist.objects.all()
        serializer = ArtistSerializer(artist, many=True)
        return Response(data=serializer.data)
    
class AlbomAPIView(APIView):
    def get(self, request):
        alboms = Albom.objects.all()
        serializer = AlbomSerializer(alboms, many=True)
        return Response(data=serializer.data)
    
class SongsAPIView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(data=serializer.data)