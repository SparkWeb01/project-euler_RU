def calc():
	s = 200
	a = [1] + [0] * s
	for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
		for i in range(len(a) - coin):
			a[i + coin] += a[i]
	return str(a[-1])

	print(calc())