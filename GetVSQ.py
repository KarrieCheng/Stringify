import spotipy
import pdb
from auth import getAuth, getUserId
from sets import Set
sp = spotipy.Spotify(auth=getAuth())

def get_user_data_total_liked_tracks(sp):
    return sp.current_user_saved_tracks()['total']


def create_song_set(sp, total):
    songs = Set([])
    i = 0 
    while i < total:
        i += 20
        tracks = sp.current_user_saved_tracks(20, i)
        for c, t in enumerate(tracks['items']):
            if (t['track']['album']['artists'][0]['name'] != 'Vitamin String Quartet'):
                songs.add(t['track']['name'].encode('ascii', 'ignore'))
    return songs

def get_total_artist_album(artist):
    return sp.artist_albums(artist,'album', 'US')['total']

def get_artist_albums(artist):
    albums = {}
    i = 0
    while i < get_total_artist_album(artist):
        i += 20
        response = sp.artist_albums(artist,'album', 'US', 20, i)
        for c, t in enumerate(response['items']):
            albums[t['name']] = t['uri']
    return albums

def get_artist_songs(albums):
    songs = {}
    for key, value in albums.iteritems():
        response = sp.album_tracks(value)
        for song in response['items']:
            songs[song['name']] = song['uri']
    return songs
    

def get_user_matched_songs(user_songs, cover_artist_songs):
    matched_songs = Set([])
    for song in user_songs:
        if(song in cover_artist_songs):
            matched_songs.add((cover_artist_songs[song].encode('ascii', 'ignore')))
    return matched_songs



cover_artist_id = '6MERXsiRbur2oJZFgYRDKz'
playlist = ''

total_liked_tracks = get_user_data_total_liked_tracks(sp)
user_liked_songs = create_song_set(sp, total_liked_tracks)
artist_songs = get_artist_songs((get_artist_albums(cover_artist_id)))
playlist_songs = Set([])
if (len(user_liked_songs) < len(artist_songs)):
    playlist_songs = get_user_matched_songs(user_liked_songs, artist_songs)
matched_songs = list(playlist_songs)
#TODO: Change to loop through the match songs because of the limit
sp.user_playlist_add_tracks(getUserId(), playlist, matched_songs)


# get_artist_albums(cover_artist_id)


#print(create_song_dictionary(sp, total_liked_tracks))


