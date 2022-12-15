with open('text.txt', 'r') as file:
    data = file.read()
    
file.close()
data = data.lower()

st = input("введите поисковый запрос по файлу text.txt:")
st = st.lower()

a = data.find(st)

while a!=-1:
	s=""

	while a-1 >= 0 and (data[a-1] != '.' and data[a-1] != '?' and data[a-1] != ';'):
		a-=1

	while a<len(data) and (data[a] != '.' and data[a] != '?' and data[a] != ';'):
		s+=data[a]
		a+=1

	print("-->>" , s)
	data = data[a:]
	a = data.find(st)