import itertools


def calc():
	a = max(range(1, 1000), key=nel)
	return str(a)


def nel(k):#функция обратная len 
	b = {}
	x = 1
	for i in itertools.count():
		if x in b:
			return i - b[x]
		else:
			b[x] = i
			x = x * 10 % k

	print(calc())