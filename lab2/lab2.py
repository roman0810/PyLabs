flag = "1"
flag = input("нажмите enter чтобы начать поиск пердолжений по файлу text.txt")

if flag = "":
	with open('text.txt', 'r') as file:
	    data = file.read()

	file.close()
	data = data.lower()

	st = input("введите слово или последовательность слов через пробел чтобы найти предложения их содержащие: ")
	st = st.lower()
	st.replace("  " , " ")

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