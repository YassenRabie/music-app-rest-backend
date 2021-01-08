from rest_framework import serializers

from .models import Artist, Album, Song

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('artist_name', 'artist_birthday')

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('album_name', 'publish_date', 'artist')
        depth = 1

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ('song_name', 'song_playtime', 'artist', 'album')
        depth = 1