def calc():
	a = sum(i for i in range(1000000) if pal(i))
	return str(a)


def pal(n):
	s = str(n)
	if s != s[ : : -1]:# отсеиваем не полиндромы
		return False
	t = bin(n)[2 : ]
	return t == t[ : : -1]

	print(calc())