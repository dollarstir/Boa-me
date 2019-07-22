from gpiozero import Button

import requests
import json

import geocoder
g = geocoder.ip('me')
print(g.latlng)

latitude =g.lat
longitude=g.lng


policebutton=Button(2)
firebutton=Button(3)
ambulancebutton=Button(4)
#a function to count the number of times a button is pressed
    

send_url = 'http://api.ipstack.com/156.38.115.11?access_key=7ae0ee9cacb82c78fb0780aaefafda41&format=1'
r = requests.get(send_url)
j = json.loads(r.text)
lat = j['latitude']
lon = j['longitude']
city=j['city']
reg=j['region_name']



def police():
        print(  "hi, I am in need of the police At",latitude,longitude,city,reg )
def fire ():
        print(  "hi , I am in need of the fire service team at",latitude,longitude,city,reg )
def ambulance():
        print(  "hi , I am in need of the ambulance team at",latitude,longitude,city,reg )
policebutton.when_pressed =police
firebutton.when_pressed =fire
ambulancebutton.when_pressed =ambulance


