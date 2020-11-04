import eulerlib, itertools

def calc():
	ans = sum(itertools.islice(filter(ysec, itertools.count(10)), 11))
	return str(ans)

def ysec(n):
	# можно ли убрать слева
	i = 10
	while i <= n:
		if not eulerlib.is_prime(n % i):#is_prime-проверка первичности
			return False
		i *= 10
	
	# можно ли убрать справа
	while n > 0:
		if not eulerlib.is_prime(n):
			return False
		n //= 10
	return True

	print(calc())