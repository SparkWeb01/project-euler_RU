def eratosthen(n): #пропускаем через решето массива от 0 до n 
    sieve = list(range(n)) #создаем лист до 2 миллионов
    sieve[1] = 0 #обнуляем элемент
    for i in sieve[2:]:
            for j in range(i + i, len(sieve), i):#прогоняем через циклы
                sieve[j] = 0 #присваеваем каждому значению нолик
    return sieve #возвращаем  назад

print(sum(eratosthen(2000000))) #передаем значение в функцию  и все суммируем