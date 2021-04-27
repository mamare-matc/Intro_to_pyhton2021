#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

#function to go to th dpecified URL and get the HTML
response = requests.get('https://notpurple.com')

#response.raise_for_status()
noPurpleSoup = BeautifulSoup(response.text, 'html.parser')
type(noPurpleSoup)

#Print the title of the page
print("Title of the website is:")
for title in noPurpleSoup.find_all('title'):
    print(title.get_text())
    
#print all links on the page
print("Links on the page: ")
for link in noPurpleSoup.find_all('a'):
    print(link.get_text())

