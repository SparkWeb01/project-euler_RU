def listmult(lst):
    s=1
    for i in lst:
        s*=i
    return s
def fibs(stop,step):
    p=step
    fib=[]
    while True:
        for n in range(p-(p-1),p):
            for m in range(p-(p-2),p+1):
                if m>n:
                    fib=[2*n*m,(m**2)-(n**2),(m**2)+(n**2)]
                    if sum(fib)==stop:
                        return listmult(fib)
        p+=step
print(fibs(1000,100))