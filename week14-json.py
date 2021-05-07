#!/usr/bin/env python3
import json
import requests
import argparse

parser = argparse.ArgumentParser(description='this is the IP address')

parser.add_argument('-ip', '--address', dest='varIP', metavar='[IP address]', type=str, help='Enter ip address of the host', 
required=False)

args = parser.parse_args()
url = f"http://ipinfo.io/{args.varIP}/json"
json_raw = requests.get(url)
myDict = json.loads(json_raw.text)

    
#for each key in  the dict print key and value
for key in myDict.keys():
	print(f"{key: <10}:{myDict[key]: <10}")




