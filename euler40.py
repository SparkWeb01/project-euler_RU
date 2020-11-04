def calc():
	s = "".join(str(i) for i in range(1, 1000000))
	a = 1
	for i in range(7):
		a *= int(s[10**i - 1])
	return str(a)

	print(compute())