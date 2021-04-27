#!/usr/bin/env python3
import requests

response = requests.get("https://notpurple.com")

#copy it to a cale my_web_file.html
with open("my_web_file.html", "w") as hFile:
    hFile.write(response.text)

print(type(response))
print(f"Status code: {response.status_code}")
print(f"Test: {response.text[:250]}")



