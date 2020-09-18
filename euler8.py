def arg_mult(b,a):
    s=1
    while b<=a:
        s*=int(arg[b])
        b+=1
    return s

def get_args(n):
    res=[]
    for i in range(0,len(arg)-(n-1)):
        res.append(arg_mult(i,i+(n-1)))
    return res

print(max(get_args(13)))