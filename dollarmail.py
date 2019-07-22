from gpiozero import Button

import requests
import json
import smtplib

import geocoder

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


getto = ["rfire@protonmail.com","rpolice@protonmail.com","rambulance@protonmail.com"]
getsubject= "I NEED HELP !!!!!"


#Mail parameters

s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
MY_ADDRESS="rasppiproject100@gmail.com"
PASSWORD="lola1997@naj"
s.login(MY_ADDRESS, PASSWORD)


msg = MIMEMultipart() 


#end mail


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
        m1=(  "hi, I am in need of the police At",latitude,longitude,city,reg )

        # set up the SMTP server

        message_template = m1
            
        message= message_template 

        msg['From']=MY_ADDRESS
        msg['To']=getto[1]
        msg['Subject']=getsubject
                
                # add in the message body
        msg.attach(MIMEText(message, 'plain'))
                
                # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
                
            # Terminate the SMTP session and close the connection
        s.quit()


def fire ():
        m2=(  "hi , I am in need of the fire service team at",latitude,longitude,city,reg )
       

        # set up the SMTP server

        message_template = m2
            
        message= message_template 

        msg['From']=MY_ADDRESS
        msg['To']=getto[0]
        msg['Subject']=getsubject
                
                # add in the message body
        msg.attach(MIMEText(message, 'plain'))
                
                # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
                
            # Terminate the SMTP session and close the connection
        s.quit()
def ambulance():
        m3=(  "hi , I am in need of the ambulance team at",latitude,longitude,city,reg )

         # set up the SMTP server

        message_template = m3
            
        message= message_template 

        msg['From']=MY_ADDRESS
        msg['To']=getto[2]
        msg['Subject']=getsubject
                
                # add in the message body
        msg.attach(MIMEText(message, 'plain'))
                
                # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
                
            # Terminate the SMTP session and close the connection
        s.quit()
policebutton.when_pressed =police
firebutton.when_pressed =fire
ambulancebutton.when_pressed =ambulance





