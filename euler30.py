def calc():
	a = sum(i for i in range(2, 1000000) if i == degree(i))#суммируем все числа
	return str(a)

def degree(k):#возводим в степень
	return sum(int(b)**5 for b in str(k))

	print(calc())