from flickrapi import FlickrAPI
from django.conf import settings

def get_flickr_client():
    return FlickrAPI(
        settings.FLICKR_API_KEY,
        settings.FLICKR_API_SECRET,
        format='parsed-json'
    )

def get_user_albums(user_id):
    flickr = get_flickr_client()
    try:
        # Get photosets (albums)
        photosets = flickr.photosets.getList(user_id=user_id)
        return photosets['photosets']['photoset']
    except Exception as e:
        print(f"Error fetching albums: {e}")
        return [] 