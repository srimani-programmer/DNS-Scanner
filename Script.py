# DNS Scanner: A python Dns lookup Tool.
# Done by @Sri_Programmer
# python v3.x

# Modules import

import requests
import json
import sys
import random
import time

__author__ = 'Sri Manikanta Palakollu.'

class Scanner:

    def __init__(self):

        # Colors for the program

        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
    
        self.api = "https://dns-api.org/"
        try:
            self.printLogo()
            self.domainName = input(self.c + 'Enter your domain name:' + self.c)
            self.scanningARecords()
        except KeyboardInterrupt:
            print(self.r + '\n [!] An Keyboard Interrupt Occured. [!]' + self.r)
            quit()

    def scanningARecords(self):
        '''A Records are the most basic type of DNS record and 
         are used to point a domain or subdomain to an IP address.'''

        response = requests.get(self.api+ 'A/' + self.domainName)
        try:
            if response.status_code == 200: # Getting the +ve response. 
                responseDate = response.text
                json_object = json.loads(responseDate)
                ttl1 = json_object[0]['ttl']
                ip1  =  json_object[0]['value']
                print(self.y + '\nStarting the A Record Scan\n' + self.y)
                print('-' * 30)
                print(self.y + "\nFirst A Record: " + ip1 + " | TTL: " + ttl1 + self.y)
                print(self.y + 'Completed A Record Scan Sucessfully...!\n' + self.y)
                print(self.rr + '\nStarting the MX-Records Scan\n' + self.rr)
                print('-' * 30)
                self.scanningMXRecords()

            else:
                print(self.y + '\n Bad Response' + self.y)
                print(self.y +'Status Code of the Scan: {}'.format(response.status_code) + self.y)
                print(self.rr +'\n Starting the MX-Records Scan\n' + self.rr)
                print('-' * 30)
                self.scanningMXRecords()

        except IndexError:
            print(self.r + 'Failed To Find A Records' + self.r)
            print(self.rr + 'Starting the MX-Records Scan' + self.rr)
            print('-' * 30)
            self.scanningMXRecords()
        except KeyError:
            print(self.r + 'Failed To Find \'A\' Records' + self.r)
            print(self.rr + 'Starting the MX-Records Scan' + self.rr)
            print('-' * 30)
            self.scanningMXRecords()

    def scanningMXRecords(self):
        '''(MX record) is a type of resource record in the Domain Name System that specifies a mail server
             responsible for accepting email messages on behalf of a recipient's domain'''
        
        response = requests.get(self.api + 'MX/' + self.domainName)

        try:
            if response.status_code == 200:
                response_data = response.text
                json_obj = json.loads(response_data)
                value1 = json_obj[0]['value']
                value2 = json_obj[1]['value']
                ttlmx1 = json_obj[0]['ttl']
                ttlmx2 = json_obj[1]['ttl']
                print(self.rr + "First MX Scan Record: " + value1.replace("10    ","").replace("com.","com") + " | TTL: " + ttlmx1 + self.rr)
                print(self.rr + "Second MX Scan Record: " + value2.replace("10    ","").replace("com.","com") + " | TTL: " + ttlmx2 + self.rr)
                print(self.rr + 'Completed the MX Records Scan Sucessfully...!\n' + self.rr)
                print(self.w + '\nStarting the AAAA Record Scan\n' + self.w)
                print('-' * 30)
                self.scanningAAAARecords()
            
            else:
                print(self.rr + 'Bad Response' + self.rr)
                print(self.rr + 'Status Code of the Scan: {}'.format(response.status_code) + self.rr)
                print(self.w + '\nStarting the AAAA Record Scan' + self.w)
                print('-' * 30)
                self.scanningAAAARecords() 
        
        except IndexError:
            print(self.r + 'Failed to find Mx Scanning records.' + self.r)
            print(self.w + '\nStarting the AAAA Record Scan' + self.w)
            print('-' * 30)
            self.scanningAAAARecords()
        
        except KeyError:
            print(self.r + 'Failed to find Mx Scanning records.' + self.r)
            print(self.w + '\nStarting the AAAA Record Scan' + self.w)
            print('-' * 30)
            self.scanningAAAARecords()

    def scanningAAAARecords(self):
        '''The record AAAA (also quad-A record) specifies IPv6 address for given host. 
           So it works the same way as the A record and the difference is the type of IP address'''

        response = requests.get(self.api + 'AAAA/' + self.domainName)

        try:
            if response.status_code == 200:
                response_data = response.text
                json_obj = json.loads(response_data)
                ttl = json_obj[0]['ttl']
                ipv6 = json_obj[0]['value']
                print(self.w  + 'AAAA Scan Record: TTL : {} | ipv6 Address: {}'.format(ttl,ipv6) + self.w)
                print(self.w + 'AAAA Scan completed Sucessfully\n' + self.w)
                print(self.c + '\nStarting the TXT Record Scan\n' + self.c)
                print('-' * 30)
                self.scanningTXTRecord()
            else:
                print(self.w + 'Bad Response' + self.w)
                print(self.w + 'Status Code of the Scan: {}'.format(response.status_code) + self.w)
                print(self.c + '\nStarting the TXT Record Scan' + self.c)
                print('-' * 30)
                self.scanningTXTRecord()
        
        except IndexError:
            print(self.r + '\nFailed to find Some AAAA Scanning records.' + self.r)
            print(self.c + '\nStarting the TXT Record Scan' + self.c)
            print('-' * 30)
            self.scanningTXTRecord()
        
        except KeyError:
            print(self.r + '\nFailed to find some AAAA Scanning records.' + self.r)
            print(self.c + '\nStarting the TXT Record Scan' + self.c)
            print('-' * 30)
            self.scanningTXTRecord()

    def scanningTXTRecord(self):

        '''
         A TXT record (short for text record) is a type of resource record in the 
         Domain Name System (DNS) used to provide the ability to associate arbitrary text with a host or other name,
         such as human readable information about a server, network, data center, or other accounting information.
        '''

        response = requests.get(self.api + 'TXT/' + self.domainName)

        try:
            if response.status_code == 200:
                response_data = response.text
                json_obj = json.loads(response_data)
                value1 = json_obj[0]['value']
                ttl1 = json_obj[0]['ttl']
                print(self.c + "First TXT Scan Record: " + value1 + " | TTL: " + ttl1)
                value2 = json_obj[1]['value']
                ttl2 = json_obj[1]['ttl']
                print("Second TXT Scan Record: " + value2 + " | TTL: " + ttl2)
                print('\nDNS Lookup scan Completed.\n' + self.c)
            else:
                print(self.c + 'Bad Response')
                print('Status Code of the Scan: {}'.format(response.status_code) + self.c)
        
        except IndexError:
            print(self.r + 'Failed to scan some records...!' + self.r)
            print(self.c + '\nDNS Lookup scan Completed.\n' + self.c)
        
        except KeyError:
            print(self.r + 'Failed to scan some records...!' + self.r)
            print(self.c + '\nDNS Lookup scan Completed.\n' + self.c)

    def printLogo(self):

        colors = [36, 32, 34, 35, 31, 37]
        clear = "\x1b[0m"

        logo =  '''



 ____  _   _ ____ ____   ____    _    _   _ _   _ _____ ____  
|  _ \| \ | / ___/ ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
| | | |  \| \___ \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
| |_| | |\  |___) |__) | |___ / ___ \| |\  | |\  | |___|  _ < 
|____/|_| \_|____/____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\

         
         
         
         Done by Sri Manikanta Palakollu.  
         Note! : I don't Accept any responsibility for any illegal usage 

        '''
        for N,line in enumerate(logo.split('\n')):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)

Scanner()