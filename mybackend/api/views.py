from rest_framework import viewsets

from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from .models import Artist, Album, Song

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('artist_name')
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('album_name')
    serializer_class = AlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('song_name')
    serializer_class = SongSerializer