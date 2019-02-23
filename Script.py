# Dns lookup Tool.

# Modules import

import requests
import json

__author__ = 'Sri Manikanta Palakollu.'
class Scanner:

    def __init__(self):
        self.api = "https://dns-api.org/"
        self.domainName = input('Enter your domain name:')
        self.scanningARecords()

    def scanningARecords(self):
        '''A Records are the most basic type of DNS record and 
         are used to point a domain or subdomain to an IP address.'''

        response = requests.get(self.api+ 'A/' + self.domainName)
        try:
            if response.status_code == 200: # Getting the +ve response. 
                responseDate = response.text
                json_object = json.loads(responseDate)
                '''
                domain_name = json_object[0]['name']
                ttl_value = json_object[0]['ttl']
                typeOfScan = json_object[0]['type']
                ipAddress = json_object[0]['value']
                '''
                ttl1 = json_object[0]['ttl']
                ip1  =  json_object[0]['value']
                print("First A Record: " + ip1 + " | TTL: " + ttl1)
                ttl2 = json_object[1]['ttl']
                ip2 = json_object[1]['value']
                print("Second A Record: " + ip2 + " | TTL " + ttl2)
                '''
                print('Domain Name: {}'.format(domain_name))    # Domain Name
                print('Ttl Value is: {}'.format(ttl_value))     # TTL value.
                print('Type of Scan: {}'.format(typeOfScan))    # Type of Scan
                print('Ip Address Of Domain: {}'.format(ipAddress)) # IpAddress
                '''
                print('Dns Lookup Scanning completed Sucessfully...!')
                print('Starting the MX-Records Scan')
                self.scanningMXRecords()

            else:
                print('Bad Response')
                print('Status Code of the Scan: {}'.format(response.status_code))
                print('Starting the MX-Records Scan')
                self.scanningMXRecords()

        except IndexError:
            print('Failed To Find A Records')
            print('Starting the MX-Records Scan')
            self.scanningMXRecords()
        except KeyError:
            print('Failed To Find \'A\' Records')
            print('Starting the MX-Records Scan')
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
                print("First MX Scan Record: " + value1.replace("10    ","").replace("com.","com") + " | TTL: " + ttlmx1)
                print("Second MX Scan Record: " + value2.replace("10    ","").replace("com.","com") + " | TTL: " + ttlmx2)
                print('Completed the MX Records Scan Sucessfully...!')
                print('Starting the AAAA Record Scan')
                self.scanningAAAARecords()
            
            else:
                print('Bad Response')
                print('Status Code of the Scan: {}'.format(response.status_code))
                self.scanningAAAARecords()
   
        
        except IndexError:
            print('Failed to find Mx Scanning records.')
            print('Starting the AAAA scan.')
            self.scanningAAAARecords()
        
        except KeyError:
            print('Failed to find Mx Scanning records.')
            print('Starting the AAAA scan.')
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
                print('AAAA Scan Record: TTL : {} | ipv6 Address: {}'.format(ttl,ipv6))
                print('AAAA Scan completed Sucessfully')
                print('Starting the TXT Record Scan')
                # self.scanningTXTRecord()
            else:
                print('Bad Response')
                print('Status Code of the Scan: {}'.format(response.status_code))
                print('Starting the TXT Record Scan')
                # self.scanningTXTRecord()
        
        except IndexError:
            print('Failed to find Some AAAA Scanning records.')
            print('Starting the TXT Record scan.')
            # self.scanningTXTRecord()
        
        except KeyError:
            print('Failed to find some AAAA Scanning records.')
            print('Starting the TXT Record scan.')
            # self.scanningTXTRecord()
        

Scanner()

        