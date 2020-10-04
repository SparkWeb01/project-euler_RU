import eulerlib, itertools


def calc():
	ans = max(((a, b) for a in range(-999, 1000) for b in range(2, 1000)),key=ppc)
	return str(ans[0] * ans[1])


def ppc(ab):#счет простых чисел
	a, b = ab
	for i in itertools.count():
		n = i * i + i * a + b
		if not is_prime(n):
			return i


main_c = eulerlib.list_primality(1000)#основной кеш

def is_prime(n):
	if n < 0:
		return False
	elif n < len(main_c ):
		return main_c [n]
	else:
		return eulerlib.is_prime(n)

	print(calc())