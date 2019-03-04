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
import requests
oath2 = "Bearer BQAW6CPwqE5iwYsEiK9jAtejt-iDXqnHcTNllacRcS0r6DNsGU5jDjErYGRKlj_joHrhhYnNUaoaHp2cFGC_oAVpjn0AHTCNKIu9krbGovwV3X0ebJnPggMWVoPSW5oof-Aj_VQl6cyY99XauTWQgqiyuIIY"
response = requests.get("https://api.spotify.com/v1/me/tracks?limit=1", headers={'Authorization': "BQAW6CPwqE5iwYsEiK9jAtejt-iDXqnHcTNllacRcS0r6DNsGU5jDjErYGRKlj_joHrhhYnNUaoaHp2cFGC_oAVpjn0AHTCNKIu9krbGovwV3X0ebJnPggMWVoPSW5oof-Aj_VQl6cyY99XauTWQgqiyuIIY"
})

print(response)