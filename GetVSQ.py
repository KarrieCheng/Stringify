'''

Get current user's saved tracks' names
 - Create Hash Table
 - Populate the container
    - Loop through the get_Saved_Tracks
    - Get total number of saved tracks
    - Loop and add until getting the number
    https://developer.spotify.com/console/get-current-user-saved-tracks/


Get all of VSQ's songs
- get VSQ Id
    - 6MERXsiRbur2oJZFgYRDKz
- instantiate list of ids
- get list of VSQ albums
    - https://developer.spotify.com/console/get-artist/?id=6MERXsiRbur2oJZFgYRDKz
    - get songs in 20 album
        - https://developer.spotify.com/documentation/web-api/reference/albums/get-several-albums/
        - https://developer.spotify.com/documentation/web-api/reference/albums/get-albums-tracks/


Compare and save the VSQ ids
    - loop through songs in albums
        - check if name is in user song dictionary
        - if yes, add song id to list

ADD ALL SONGS TO PLAYLIST
- create a playlist
- add songs to the playlist
    - https://developer.spotify.com/documentation/web-api/reference/playlists/add-tracks-to-playlist/
'''


import spotipy
from auth import getAuth
sp = spotipy.Spotify(auth=getAuth())

def get_user_data_total_liked_tracks(sp):
    return sp.current_user_saved_tracks()['total']


def create_song_dictionary(sp, total):
    i = 0
    songs = {}
    while i < 20:
        tracks = sp.current_user_saved_tracks(50, i)
        for c, t in enumerate(user_library['items']):
            if (t['track']['album']['artists'][0]['name'] != 'Vitamin String Quartet'):
                print(t['track']['album']['artists'][0]['name'],  '\n')
                songs[t['track']['name']] = 'Valid'
            else:
                print('reeee')
        i += 20
    return songs

user_library = sp.current_user_saved_tracks()
total_liked_tracks = get_user_data_total_liked_tracks(sp)
dictionary = create_song_dictionary(sp, total_liked_tracks)
#print(create_song_dictionary(sp, total_liked_tracks))


