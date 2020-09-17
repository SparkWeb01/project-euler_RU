def qsum(n): 
    su1=0 # будет хранить сумму квадратов
    su2=0 
    inD=0
    r=range(1,n+1)
    for i in r:
        su1+=(i**2) # Прибавляем квадрат числа к сумме
        su2+=(i**2)
        for j in r[inD+1:]:
            su1+=2*i*j # Умножаем число на последующие аргументы списка
        inD+=1
    return su1-su2
print(qsum(100))