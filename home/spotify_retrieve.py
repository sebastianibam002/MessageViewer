import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from random import choice

def get_random_song_from_playlist():
    dic_return = {"name_song": "", "artist_name": "", "image_height": 0, "image_width": 0, "image_url": "", "preview_url": ""}
    client_id = 'd16433eef82440cda1f68df4a39666e5'
    client_secret = 'c6cdcca4e7eb4bb69352564e11be8673'
    credentials = SpotifyClientCredentials(client_id, client_secret)
    spotify = spotipy.Spotify(client_credentials_manager=credentials)
    lz_uri = 'https://open.spotify.com/playlist/' \
            '7GBDRwuCWIlB7ukVSQ1z6i?si=c911631c488e4726'
    playlist_URI = lz_uri.split("/")[-1].split("?")[0]
    results = spotify.playlist_items(playlist_URI)
    track_pick = choice(results['items'])
    main_track = track_pick['track']
    dic_return['name_song'] = main_track['name']
    dic_return['artist_name'] = main_track['artists'][0]['name']
    dic_return['image_url'] = main_track['album']['images'][0]['url']
    dic_return['image_height'] = main_track['album']['images'][0]['height']
    dic_return['image_width'] = main_track['album']['images'][0]['width']
    dic_return['preview_url'] = main_track['preview_url']
    return dic_return

if __name__ == "__main__":
    print("Comenzando busqueda...")
    print(get_random_song_from_playlist())