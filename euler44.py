import itertools

def calc():
	pentanum = PentagonalNumberHelper()
	min_d = None  # Нет означает, что еще не найден, положительное число означает, что кандидат найден
	# Для каждого индекса верхнего пятиугольного числа, идущего вверх
	for i in itertools.count(2):
		pent_i = pentanum.term(i)
		# Если следующее число меньше, чем найденное различие, завершите поиск
		if min_d is not None and pent_i - pentanum.term(i - 1) >= min_d:
			break
		
		# Для каждого нижнего индекса пятиугольного числа, идущего вниз
		for j in range(i - 1, 0, -1):
			pent_j = pentanum.term(j)
			diff = pent_i - pent_j
			# Если разница не меньше найденной разницы, прекратите тестирование более низких пятиугольных чисел
			if min_d is not None and diff >= min_d:
				break
			elif pentanum.is_term(pent_i + pent_j) and pentanum.is_term(diff):
				min_d = diff  # Нашел меньшее различие
	return str(min_d)



class PentagonalNumberHelper:
	def __init__(self):
		self.term_list = [0]
		self.term_set = set()
	
	def term(self, x):
		assert x > 0
		while len(self.term_list) <= x:
			n = len(self.term_list)
			term = (n * (n * 3 - 1)) >> 1
			self.term_list.append(term)
			self.term_set.add(term)
		return self.term_list[x]
	
	def is_term(self, y):
		assert y > 0
		while self.term_list[-1] < y:
			n = len(self.term_list)
			term = (n * (n * 3 - 1)) >> 1
			self.term_list.append(term)
			self.term_set.add(term)
		return y in self.term_set

print(calc())