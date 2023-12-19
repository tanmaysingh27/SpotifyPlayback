import urequests as requests
import ujson
import network
import spotipy 

authCode = 'authCode'
ssid = "SSID"
password = "password"
acess_token = 'access_token'  #it is just made for the example 

grant_type = 'authorization_code'

#it is needed for some API calls
redirect_uri = 'http://localhost:5000/callback'

#get it from spotify dashboard
client_id = 'client_id'
client_secret = 'client_seceret'


wifi = network.WLAN(network.STA_IF)
wifi.active(True);
wifi.connect(ssid,password)

if(wifi.isconnected()):
    print("Connected to: ", wifi.ifconfig()[0])

#the access_token will be suplied through the api call made from the spotipy library I wrote to hanlde all the calls made for the api
access_token = spotipy.token(authCode) 





