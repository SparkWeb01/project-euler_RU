import math

def calc():
	ans = sum(i for i in range(3, 10000000) if i == f(i))
	return str(ans)

def f(n):#факториальная сумма цифр
	result = 0
	while n >= 10000:
		result += FS[n % 10000]	
		n //= 10000
	return result + FB[n]
	
FB = [sum(math.factorial(int(c)) for c in str(i)) for i in range(10000)]
#FB-сумма без ведущих нулей
FS = [sum(math.factorial(int(c)) for c in str(i).zfill(4)) for i in range(10000)]
#FS-сумма с ведущими нулями

	print(calc())