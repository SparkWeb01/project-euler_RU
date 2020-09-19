def g_file(fl,k):
    f = open(fl,'r')#открываем файл для чтения
    list_fl=[]
    for i in range(k):
         t=f.readline()#считывает из файла строку 
         list_fl.append(int(t[0:50]))#добавляет эл-т в конец списка
    return list_fl
list_fl=g_file('D:\\euler13.txt',100)#делаем список
print(str(sum(list_fl))[0:10])
