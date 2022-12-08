flag = True

first = int(input())
sec = int(input())
com = input()

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
	sec = int(input())
	
	com = input()
	if com == "stop":
		flag = False
	
