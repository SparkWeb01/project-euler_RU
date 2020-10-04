def calc():#считаем сумму делителей для каждого числа
	div = [0] * 10000
	for i in range(1, len(div)):
		for j in range(i * 2, len(div), i):
			div[j] += i
	
	a = 0
	for i in range(1, len(div)):#находим все дружеские пары 
		j = div[i]
		if j != i and j < len(div) and div[j] == i:
			a += i
	return str(a)
	
	print(calc())