def is_polindrom(num):
    raw = str(num)
    r_raw = int(raw[::-1])
    if num == r_raw:
        return True
    else:
        return False

pol=[]
for i in range (100, 1000):
    for j in range(100, 1000):
        if is_polindrom(i*j) == True:
            pol.append(i*j)
print(max(pol))