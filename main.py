#!/usr/bin/env python3
import os
import spotipy
import pytube

#Import env variables

# Set your Spotify and YouTube Music API credentials
spotify_client_id = '1acc8546c9f342728de31d707aca0324'
spotify_client_secret = os.environ.get("SPOTY_SECRET")
youtube_music_api_key = os.environ.get("YT_SECRET")

redirect_uri = os.environ.get("")

# Create an OAuth2 authentication manager
auth_manager = spotipy.oauth2.SpotifyOAuth(client_id=spotify_client_id, client_secret=spotify_client_secret)

# Add the required scopes
auth_manager.scope = 'playlist-modify-private playlist-modify-public'

# Authorize the Spotify application
#auth_manager.authorize()

# Create a Spotify client object
spotify = spotipy.Spotify(auth_manager=auth_manager)

# Get the YouTube Music playlist ID
#youtube_music_playlist_id = 'PL8vb1jIneKrL3_NMnxmY1i_gcCwkgCApD'
#youtube_music_playlist_id = 'https://music.youtube.com/playlist?list=PL8vb1jIneKrL3_NMnxmY1i_gcCwkgCApD' bing chillin 1
youtube_music_playlist_id = 'https://music.youtube.com/playlist?list=PL8vb1jIneKrLko6RlwMVaR7qJFG5qT9QK'

# Get the songs in the YouTube Music playlist
youtube_music_playlist = pytube.Playlist(youtube_music_playlist_id)
youtube_music_songs = youtube_music_playlist.videos

# Create a Spotify playlist
#spotify_playlist = spotify.user_playlist_create('herrboh','Bing Chillin',public=True,collaborative=False,description='Powered by python')
spotify_playlist = '37ZZHmC1dnehizTn6jW9fE'

# Add the songs from the YouTube Music playlist to the Spotify playlist
tracks = []
for youtube_music_song in youtube_music_songs:
    spotify_song = spotify.search(q=youtube_music_song.title, type='track')
    spotify_playlist_track_id = spotify_song['tracks']['items'][0]['id']
    tracks.append(spotify_playlist_track_id)
spotify.user_playlist_add_tracks('herrboh',spotify_playlist, tracks,position=None)
#if you are creating playlis, tsecond argument is spotify_playlist['id'] 
#if you are using an existing playlist, second argument is the already existing spotify ID (found in the playlist URL)


# Print a success message
print('Your YouTube Music playlist has been successfully imported to Spotify!')


