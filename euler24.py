import itertools

def calc():
	a = list(range(10))
	temp = itertools.islice(itertools.permutations(a), 999999, None)
	# permutations делает:permutations(range(3)) --> 012 021 102 120 201 210
	return "".join(str(i) for i in next(t))# собираем строку

	print(calc())