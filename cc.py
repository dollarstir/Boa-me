from gpiozero import Button
import geocoder
g = geocoder.ip('me')
print(g.latlng)

latitude =g.lat
longitude=g.lng


policebutton=Button(2)
firebutton=Button(3)
ambulancebutton=Button(4)
#a function to count the number of times a button is pressed
    


def police():
        print(  "hi, I am in need of the police At",latitude,longitude )
def fire ():
        print(  "hi , I am in need of the fire service team at")
def ambulance():
        print(  "hi , I am in need of the ambulance team at")
policebutton.when_pressed =police
firebutton.when_pressed =fire
ambulancebutton.when_pressed =ambulance
