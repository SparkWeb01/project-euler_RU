import eulerlib

def calc():
	ans = sum(i for i in range(1, 10000) if pan(i))
	return str(ans)

def pan(n):
	# поиск всех факторов n
	for i in range(1, eulerlib.sqrt(n) + 1):
		if n % i == 0:
			temp = str(n) + str(i) + str(n // i)
			if "".join(sorted(temp)) == "123456789":
				return True
	return False

	print(calc())
