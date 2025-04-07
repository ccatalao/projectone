from django.db import models
from django.utils import timezone

class FlickrAlbum(models.Model):
    flickr_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    cover_photo_url = models.URLField(max_length=500)
    photo_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class FlickrPhoto(models.Model):
    flickr_id = models.CharField(max_length=100, unique=True)
    album = models.ForeignKey(FlickrAlbum, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=500)
    thumbnail_url = models.URLField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.title
