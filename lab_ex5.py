a=input('введите число ')
a=int(a)
b=input('введите второе чисоло ')
b=int(b)
if a%b==0:
    s=a/b
    print (a, 'делится на', b, 'частное =', s)
else:
    n=a/b
    print (a, 'не делится нацело на', b,',', a, '/', b, '=', n)