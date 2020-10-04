def calc():
	m = 28124 
	div = [0] * m
	for i in range(1, m):
		for j in range(i * 2, m, i):
			div[j] += i
	a = [i for (i, x) in enumerate(div) if x > i]
	
	b = [False] * m
	for i in a:
		for j in a:
			if i + j < m:
				b[i + j] = True
			else:
				break
	
	a = sum(i for (i, x) in enumerate(b) if not x)# суммируем все числа которые не могут быть записаны
	return str(a)

	print(calc())
