from django.shortcuts import render
from .models import FlickrAlbum, FlickrPhoto

# Create your views here.

def album_list(request):
    albums = FlickrAlbum.objects.all()
    return render(request, 'flickr_gallery/album_list.html', {'albums': albums})

def album_detail(request, album_id):
    album = FlickrAlbum.objects.get(flickr_id=album_id)
    photos = album.photos.all()
    return render(request, 'flickr_gallery/album_detail.html', {
        'album': album,
        'photos': photos
    })
