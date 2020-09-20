exception={
	1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    15:'fifteen',
    18:'eighteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
}

def generator(k,s):
 t=''
 l=str(k)
 if s.get(k,False):
    return s[k]
 elif k<20:
     return s[int(l[1])]+'teen'
 elif k<100:
     t=k-int(l[1])
     return s[t]+s[int(l[1])]
 elif k<1000:
     if l[1:3]=='00':
      return s[int(l[0])]+'hundred'
     else:
      return s[int(l[0])]+'hundredand'+generator(int(l[1:3]),exception)
 elif k==1000:
     return 'onethousand'

p=0
for i in range(1,1001):
    p+=len(generator(i,exception))
    print(generator(i,exception))
print(p)