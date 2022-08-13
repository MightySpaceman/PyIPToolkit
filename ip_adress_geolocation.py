import geocoder
import socket
import os

def website_ip():
        website_name = input('==== Enter Website To Grab IP ====\n')
        get_ip = socket.gethostbyname(website_name)
        ip = geocoder.ip(get_ip)
        print('\nName: ',website_name)
        print('\nServer IP: ',get_ip)
        print('\nServer City: ',ip.city,', ',ip.country)
        print('\nServer Lattitude/Longtitude: ',ip.latlng,'\n')


def direct_ip():
        while True:
         direct_ip = input('==== Enter IP adress ====\n')
         ip = geocoder.ip(direct_ip)
         print('\nStatistics for ',direct_ip)
         print('\nCity: ',ip.city,', ',ip.country)
         print('\nLattitude/Longtitude: ',ip.latlng,'\n')
        


while True:
    question_answer = input('==== Find out website IP adress (y), or get location of direct IP adress? (n) ====\n')
    if question_answer == 'y':
        website_ip()

    elif question_answer == 'n':
        direct_ip()
        
    else:
        print('Invalid answer. please try again.')

        
