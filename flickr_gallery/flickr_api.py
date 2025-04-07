from flickrapi import FlickrAPI
from django.conf import settings
import os
import json

def get_flickr_client():
    """
    Returns an authenticated FlickrAPI client
    """
    # Verify API credentials
    api_key = settings.FLICKR_API_KEY
    api_secret = settings.FLICKR_API_SECRET
    
    if not api_key or not api_secret:
        raise ValueError("Flickr API credentials are missing. Please check your .env file.")
    
    print(f"Using API Key: {api_key[:5]}...")  # Only show first 5 chars for security
    
    # Create FlickrAPI instance with authentication
    flickr = FlickrAPI(
        api_key,
        api_secret,
        format='parsed-json',
        store_token=False  # Don't store token in file
    )
    
    return flickr

def get_user_albums(user_id):
    """
    Fetches all albums (photosets) for a given user
    """
    flickr = get_flickr_client()
    try:
        # Try to get all albums, including private ones
        response = flickr.photosets.getList(
            user_id=user_id,
            primary_photo_extras='url_sq,url_t,url_s,url_m,url_o',
            privacy_filter=1  # Show all albums (1=public, 2=private, 3=public and private)
        )
        
        print("API Response:", response)  # Debug output
        
        if 'photosets' in response and 'photoset' in response['photosets']:
            albums = response['photosets']['photoset']
            print(f"Found {len(albums)} albums")
            return albums
        else:
            print("Unexpected response format:", response)
            return []
            
    except Exception as e:
        print(f"Error fetching albums: {str(e)}")
        return [] 