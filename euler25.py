import itertools

def calc():
	ts = 1000
	a = 1
	k = 0
	for i in itertools.count():#вычисляем каждое число фибоначи
		if len(str(k)) > ts:
			raise RuntimeError("Not found")
		elif len(str(k)) == ts:
			return str(i)
		#продвигаем последовательность на 1 шаг
		a, k = k, a + k

	print(calc())