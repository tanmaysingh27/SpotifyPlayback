import urequests as requests
import ujson
import network
import utime
import _thread
import spotipy as spotify 

authCode = 'authCode'
ssid = "SSID"
password = "Password"

#Connecting to WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True);
wifi.connect(ssid,password)

if(wifi.isconnected()):
    print("Connected to: ", wifi.ifconfig()[0])

tokens = spotify.tokens(authCode)
while true:
    playback_state = spotify.playback_state(tokens['access_token'])





