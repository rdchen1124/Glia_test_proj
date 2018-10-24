# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs4
result = requests.get('https://www.ptt.cc/bbs/NBA/index.html')
content = result.content
soup = bs4(content, "html.parser")
# divs = soup.select('div#main-container > div.r-list-container > div.r-ent')
divs = soup.find_all("div", class_="r-ent")
for div in divs:
	title = div.find("div", {"class" : "title"})
	url = title.a.get('href')
	author = div.find("div", {"class" : "author"}).text
	date = div.find("div", {"class" : "date"}).text
	print(title.text)
	print(url)
	print(author)
	print(date)
# print(soup)