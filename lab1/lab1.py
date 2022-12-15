flag = True

first = int(input("введите первое число: "))
sec = int(input("введите второе число: "))
com = input("введите операцию для вашей пары числел: ")

while flag:
	if com == "*":
		res = first*sec
	elif com == "/" and sec != 0:
		res = first/sec
	elif com == "+":
		res = first+sec
	elif com == "-":
		res = first-sec
	else:
		res = None

	print("-->> " , res)
	first = res
	sec = int(input("введите второе число: "))
	
	com = input("введите операцию или stop если не хотите продолжать: ")
	if com == "stop":
		flag = False
	
