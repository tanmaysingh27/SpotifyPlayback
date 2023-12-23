import urequests as requests
import ujson

grant_type = 'authorization_code'
grant_type_refresh = 'refresh_token'
redirect_uri = 'http://localhost:5000/callback'
client_id = 'client_id'
client_secret = 'client_seceret'
token_endpoint = 'https://accounts.spotify.com/api/token'
player_endpoint = 'https://api.spotify.com/v1/me/player?market=IN'


#This function is the first function to run, it generates the first authrization token and refresh token and passes to the main function
def tokens(code):
    
    payload = {
    "grant_type": grant_type,
    "code": code,
    "redirect_uri": redirect_uri,
    "client_id": client_id,
    "client_secret": client_secret
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    
    data = "&".join([f"{key}={value}" for key, value in payload.items()]).encode()
    response = requests.post(token_endpoint,data = data,headers = headers)
    
    response_data = response.json()
    print(response_data['access_token'])
    access_token = response_data['access_token']
    print(response_data['refresh_token'])
    refresh_token = response_data['refresh_token']

    tokens = {'access_token':access_token,'refresh_token':refresh_token}
    return tokens

#This function uses the spotify endpoint to get the playback data
def playback_state(access_token,):
    
    authorization ='Bearer '+access_token
    headers = {"Authorization": authorization}
    
    response = requests.get(player_endpoint, headers = headers)
    data = response.json()

    playback_data = {
        'deviceName':data['device']['name'],
        'artist':data['item']['artists'][0]['name'],
        'songName':data['item']['album']['name'],
        'albumPic':data['item']['album']['images'][1],
        'pause':data['is_playing'],
        'progress':data['progress_ms'],
        'duration':data['item']['duration_ms']        
        }
    return playback_data

#This uses refresh token to generate a new access token to be used when expires     
def referesh_token(refresh_token):
    
    payload = {
    "grant_type": grant_type_refresh,
    "refresh_token": refresh_token,
    "client_id": client_id,
    "client_secret": client_secret
    }
    
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    
    data = "&".join([f"{key}={value}" for key, value in payload.items()]).encode()
    response = requests.post(token_endpoint,data = data,headers = headers)
    response_data = response.json()
    print(response_data['access_token'])
    
