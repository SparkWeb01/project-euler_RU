def calc():
	a = set(a**b for a in range(2, 101) for b in range(2, 101))#создаем множество из степеней
	return str(len(a))#считаем

	print(calc())