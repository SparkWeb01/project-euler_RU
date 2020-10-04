def compute():
	s = 1001 
	a = 1  
	a += sum(4 * n * n - 6 * (n - 1) for n in range(3, s + 1, 2))#4n ^ 2 - 6 (n - 1)(где n нечетное)
	return str(a)

	print(compute())