#!/usr/bin/env python3
import argparse
import sys
import requests
import json
import socket
from bs4 import BeautifulSoup 

parser = argparse.ArgumentParser(description= "This is a description of your script")

#argument for a string with -ip flag
parser.add_argument('-ip', '--ip address', dest='varIP', metavar='[a string]', 
help='Enter ip address',  required=False)

#argument for integer
parser.add_argument('-f', '--integer', dest='varInteger', metavar='[an integer]', 
type=int, required=False, help='enter interger')

args = parser.parse_args()


#function to print my first and last name 
def format_name(firstname,lastname):
    return f"Name: {firstname}{lastname}"

#Fuction 1 to get response and return text
def get_response(url):
    urlone = f"http://{url}/q1"
    print(urlone)
    response = requests.get(urlone)
    return(response.text)

#function 2 takes argument url 
def parse_string(url):
   urltwo = f"http://{url}/q2"
   print(urltwo)
   get_url = requests.get(urltwo)
   get_text = get_url.text
   soup = BeautifulSoup(get_text, "html.parser")
   message = soup.find('h3').getText()
   return(message)
 
#funtion 3 return header value
def parse_header(url):
    urlthree = f"http://{url}/q3"
    print(urlthree)
    geturl = requests.get(urlthree)
    if geturl.ok:
        return geturl.headers.get("MATC-HEADER");
    else:
        print(f"there is error")
    return geturl
    
         
#fuction 4 parse_json return author of the book title
def parse_json(url):
    urlfour = f"http://{url}/q4"
    print(urlfour)
    geturl = requests.get(urlfour)
    jsondict = json.loads(geturl.text)
    dict = jsondict['Music And Books']
    for items in dict:
        if items['title'] == '1984':
            return(items['author'])
    
  
#fuction 5 socket_client
def socket_client(url):
    urlfive = f"http://{url}/q5"
    print(urlfive)
    geturlfive = 'requests.get(urlfive)'
    MYHOST = '172.31.28.253'
    MYPORTS = range(5000, 6000)
    myTimeout = 2
    snd_data = "secret"
    
    #loop to scan the port
    for MYPORT in MYPORTS:
        C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        C_SOCK.settimeout(myTimeout)
        
        try:
            C_SOCK.connect((MYHOST, MYPORT))
            RCV_DATA = C_SOCK.recv(1024).decode("utf-8")
            #print(f"connection state: {MYPORT}:: Port Open")
            if MYPORT == "port open":
                C_SOCK.send(snd_data)
                
            return RCV_DATA
            C_SOCK.close()
        except socket.error as e:
            #print(F"connection state: {MYPORT}:: Port closed")
            C_SOCK.close()
    
    
#script to call all five fuctions
if args.varInteger == 1:
    print(format_name("Mahlet "," Amare"))
    result = get_response(args.varIP)
    print(f"Answer: {result}")
elif args.varInteger == 2: 
    print(format_name("Mahlet "," Amare"))
    resulttwo = parse_string(args.varIP)
    print(f"ANSWER:  {resulttwo}")
elif args.varInteger == 3:
    print(format_name("Mahlet "," Amare"))
    resultthree = parse_header(args.varIP)
    print(f"ANSWER:  {resultthree}")
elif args.varInteger == 4:
    print(format_name("Mahlet "," Amare"))
    resultfour = parse_json(args.varIP)
    print(f"ANSWER:  {resultfour}")
elif args.varInteger == 5:
    print(format_name("Mahlet "," Amare"))
    resultfive = socket_client(args.varIP)
    print(f"ANSWER:  {resultfive}")