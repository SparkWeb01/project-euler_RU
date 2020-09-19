import math

def int_sqrt(b):
    a=math.ceil((math.sqrt(b)))
    if a*a==b:# если округленный корень числа в квадрате равен самому числу то число имеет целый корень
        return True
    else:
        return False

def max_t(c):
    a=3
    b=2
    while b<=c:
        b=2
        num=sum([i for i in range(1,a+1)])
        for k in range(2,math.ceil(math.sqrt(num))):
            if num%k==0:
                b+=2
        if int_sqrt(num):
                b-=1
        a+=1
    return num

print(max_t(500))