import itertools

def calc():
	a = sum(int("".join(map(str, n)))
		for n in itertools.permutations(list(range(10)))
		if d_p(n))
	return str(a)

#испытание деления
tst = [2, 3, 5, 7, 11, 13, 17]

#делимая подстрока
def d_p(num):
	return all((n[i + 1] * 100 + n[i + 2] * 10 + n[i + 3]) % p == 0
		for (i, p) in enumerate(tst))

print(calc())