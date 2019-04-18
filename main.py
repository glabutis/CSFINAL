from bs4 import BeautifulSoup
import requests
from tkinter import *
import csv

webPage = 'https://attheworks.org/calendar-events/'

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
    }

pageResponse = requests.get(webPage, headers=headers, timeout=5)
pageContent = BeautifulSoup(pageResponse.content, "html.parser")

file = open("data.txt", "w")



textContent = []

div = pageContent.find("div", {"class":"everydaym"})
eventsHTML = div.find_all("a")

for event in eventsHTML:
    textContent.append(event.text)

for item in textContent:
    file.write(str(item) + "\n")
    print(item)


file.close()
print("Done")
