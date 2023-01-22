import re

handle = open("text.txt" , "r" , encoding = "utf-8" , errors = "ignore")
text = handle.read()
handle.close()
text = text.replace("." , ".$")
text = text.replace("!" , "!$")
text = text.replace("?" , "?$")
text = text.replace(":" , ":$")
text = text.replace(";" , ";$")
text = text.lower()

sents = text.split("$")

rawkey = input("enter key words separated by spaces: ")
rawkey = rawkey.lower()
key = rawkey.split(" ")

regexp = r"\s";
for word in key:
	regexp += word + r"[а-яА-я]*\s+"

for s in sents:
	match = re.search(regexp , s)
	if match:
		start = match.start()
		end = match.end()
		substr = s[start:end]
		ns = s.replace(substr , substr.upper())
		print("found -->> " , ns)
