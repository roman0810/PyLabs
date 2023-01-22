import requests
from bs4 import BeautifulSoup
import re

import urllib.parse

def MakeRegFromKeyWords(rawkey):
	rawkey = rawkey.lower()
	key = rawkey.split(" ")

	regexp = r"\s";
	for word in key:
		regexp += word + r"[а-яА-я]*\s+"

	return regexp

def ProcessPage(pageurl , depth , regexp , vizited = []):
	lst = []
	if depth <= 0:
		return []
	pageurl = urllib.parse.unquote(pageurl) #удаление служебных элементов из ссылки
	if pageurl.find("http") < 0:
		pageurl = r"http://" + pageurl
	pageurl = pageurl.replace("index.html" , "")
	pageurl = pageurl.rstrip("/")

	if pageurl in vizited:
		return []
	else:
		vizited.append(pageurl)
		print("-->> обрабатываю страницу " , pageurl)
		try:
			resp = requests.get(pageurl)
			soup = BeautifulSoup(resp.text , 'lxml')
			txt = soup.text
			txt = txt.lower()
		except:
			print("--->> ссылка ", pageurl ,"не работает!")
			return []
		match = re.search(regexp , txt)
		if match:
			start = match.start()
			end = match.end()
			print("->> найдено совпадение на " , pageurl)

			s0 = start - 100
			if s0 < 0:
				s0 = 0
			e0 = end + 100
			if e0 >= len(txt):
				e0 = len(txt)-1

			print(txt[s0:e0])
			lst.append([pageurl , start , end , txt[s0:e0]])

		for tag in soup.find_all("a" , href = True):
			mas = ProcessPage(tag['href'] , depth-1 , regexp , vizited)
			for items in mas:
				lst.append(items)

		return lst

addres = input("Ведите адрес сайта: ")
key = input("Введите ключевую фразу для поиска: ")
depth = int(input("Введите поисковую глубину: "))
regexp = MakeRegFromKeyWords(key)
vizited = []
mas = ProcessPage(addres , depth , regexp , vizited)
persent = len(mas)/len(vizited) * 100.0
print("> процент совпадения ключевой фразы: " , persent)
regexp = r"https?\:?\/\/(www\.)?.\w+\.\w+(\.\w+)?(\.\w+)?(\.\w+)?(\.\w+)?"
#убираем название сайта
websites = {}
for item in mas:
	match = re.search(regexp , item[0])
	if match:
		start = match.start()
		end = match.end()
		website = item[0][start:end]
		if website in websites.keys():
			websites[website] += 1
		else:
			websites[website] = 1

print("наличие информации на сайтах:" , websites)




