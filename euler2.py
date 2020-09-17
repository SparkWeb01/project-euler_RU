f=[1,2]
i=2
a=0
while f[i]<4000000:
    f.append(f[i-1]+f[i-2])
    i+=1
    a=f[i]
res=filter(lambda x:x%2==0, f)
print(sum(res))
