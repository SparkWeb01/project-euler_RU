s = 0
for i in range(1, 4000000):

    if (i % 3 == 0) or (i % 5 == 0):
        s = s + i

print(s)