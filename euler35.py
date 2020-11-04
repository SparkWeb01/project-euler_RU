import eulerlib

def calc():
	isprime = eulerlib.list_primality(999999)
	def s(n):
		k = str(n)
		return all(isprime[int(k[i : ] + k[ : i])] for i in range(len(k)))
	
	a = sum(1 for i in range(len(isprime)) if s(i))
	return str(a)

	print(calc())