from gpiozero import Button

import requests
import json
import smtplib

import geocoder

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

# set up the SMTP server
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
MY_ADDRESS="rasppiproject100@gmail.com"
PASSWORD="lola1997@naj"
s.login(MY_ADDRESS, PASSWORD)


msg = MIMEMultipart() 
message_template = reg
    
message= message_template 

#msg['From']=MY_ADDRESS
#msg['To']="rpolice@protonmail.com"
#msg['Subject']="HELP!!!"
        
        # add in the message body
msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
s.send_message(msg)
del msg
        
    # Terminate the SMTP session and close the connection
s.quit()

services = ["rpolice@protonmail.com", "rfire@protonmailcom", "rambulance@gmail.com"]

def police():
        msg['From']=MY_ADDRESS
        msg['To']=serices["0"]
        msg['Subject']="HELP!!!"
        msg = MIMEMultipart()
        help = "Help, I am in need of the police At"
        message_template = (help, latitude,longitude,city,reg)
        message= message_template
        
def fire ():
        msg['From']=MY_ADDRESS
        msg['To']=serices["1"]
        msg['Subject']="HELP!!!"
        msg = MIMEMultipart()
        help = "Help, I am in need of the Fire Serice at"
        message_template = (help, latitude,longitude,city,reg)
        message= message_template

def ambulance():
        msg['From']=MY_ADDRESS
        msg['To']=serices[2]
        msg['Subject']="HELP!!!"
        msg = MIMEMultipart()
        help = "Help, I am in need of the Ambulance at"
        message_template = (help, latitude,longitude,city,reg)
        message= message_template
        
policebutton.when_pressed =police
firebutton.when_pressed =fire
ambulancebutton.when_pressed =ambulance