import requests
import time

URL = "https://example.com"

def get_content():
    return requests.get(URL).text

# first time save
old_content = get_content()

while True:
    time.sleep(30)  # check every 30 seconds
    new_content = get_content()

    if new_content != old_content:
        print("⚠️ Website changed!")
        old_content = new_content
    else:
        print("No change...")