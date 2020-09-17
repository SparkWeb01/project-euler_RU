import math
def issimple(n): #функция определения простого числа
    r=math.ceil(math.sqrt(n))
    for i in range(2,n): #перебираем числа до квадратного корня нужного числа
        if n%i==0:
            return False
    return True
n=5 #перебираем начиная с 5
s=[2,3]
while True:
    if issimple(n) is True:
        s.append(n)
    if len(s)==10001:#условие выхода из цикла
        break
    n+=2

print(s[-1])