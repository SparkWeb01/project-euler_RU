import eulerlib

def calc():
		a = list(reversed(range(1, n + 1)))
		while True:
			if a[-1] not in last:
				n = int("".join(str(x) for x in a))
				if eulerlib.is_prime(n):
					return str(n)
			if not per(a):
				break
	raise AssertionError()

last = {0, 2, 4, 5, 6, 8}

#предыдущие перестановки
def per(arr):
	i = len(a) - 1
	while i > 0 and a[i - 1] <= a[i]:
		i -= 1
	if i <= 0:
		return False
	j = len(a) - 1
	while a[j] >= a[i - 1]:
		j -= 1
	a[i - 1], a[j] = a[j], a[i - 1]
	a[i : ] = a[len(a) - 1 : i - 1 : -1]
	return True

print(calc())