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
csvFile = open('info.csv', mode='w+',newline='')
csvFile = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

textContent = []
for i in range(0, 5 * 3):
	paragraphs = pageContent.find_all("td")[i].text
	textContent.append(paragraphs)

for item in textContent:
    csvFile.writerow([item])
    print([item])

print("Done")
