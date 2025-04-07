from django.core.management.base import BaseCommand
from flickr_gallery.flickr_api import get_flickr_client, get_user_albums
from flickr_gallery.models import FlickrAlbum, FlickrPhoto
from django.conf import settings

class Command(BaseCommand):
    help = 'Sync Flickr albums and photos with the database'

    def handle(self, *args, **options):
        flickr = get_flickr_client()
        user_id = '153043675@N04'
        
        self.stdout.write("Fetching albums from Flickr...")
        albums = get_user_albums(user_id)
        self.stdout.write(f"Found {len(albums)} albums")
        
        # Debug: Print the first album to see its structure
        if albums:
            self.stdout.write("First album structure:")
            self.stdout.write(str(albums[0]))
        
        # Albums to exclude - only the very large ones we don't want to process
        exclude_albums = ['AUTO_UPLOAD']  # Only exclude the auto-upload album
        
        # Filter criteria
        min_photos = 1  # Minimum number of photos in an album
        max_photos = 200  # Increased from 100 to 200 to include Rota Vicentina
        
        for album in albums:
            album_title = album['title']['_content'].lower()
            photo_count = int(album['photos'])
            
            # Skip excluded albums
            if album_title in exclude_albums:
                self.stdout.write(f"Skipping excluded album: {album_title}")
                continue
                
            # Skip albums with too few or too many photos
            if photo_count < min_photos or photo_count > max_photos:
                self.stdout.write(f"Skipping album due to photo count ({photo_count}): {album_title}")
                continue
                
            # Create or update album
            flickr_album, created = FlickrAlbum.objects.update_or_create(
                flickr_id=album['id'],
                defaults={
                    'title': album['title']['_content'],
                    'description': album['description']['_content'],
                    'photo_count': album['photos'],
                    'cover_photo_url': f"https://farm{album['farm']}.staticflickr.com/{album['server']}/{album['primary']}_{album['secret']}_b.jpg"
                }
            )
            
            self.stdout.write(f"{'Created' if created else 'Updated'} album: {album['title']['_content']}")
            
            # Get photos for this album
            self.stdout.write(f"Fetching photos for {album['title']['_content']}...")
            photos = flickr.photosets.getPhotos(
                photoset_id=album['id'],
                user_id=user_id
            )['photoset']['photo']
            
            self.stdout.write(f"Found {len(photos)} photos in {album['title']['_content']}")
            
            # Update photos
            for photo in photos:
                FlickrPhoto.objects.update_or_create(
                    flickr_id=photo['id'],
                    defaults={
                        'album': flickr_album,
                        'title': photo['title'],
                        'image_url': f"https://farm{photo['farm']}.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}_b.jpg",
                        'thumbnail_url': f"https://farm{photo['farm']}.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}_q.jpg"
                    }
                )
        
        self.stdout.write(self.style.SUCCESS('Successfully synced Flickr albums and photos')) 