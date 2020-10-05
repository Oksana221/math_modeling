a=input ('введите первое число ')
a=int(a)
b=input ('введите второе число ')
b=int(b)
c=input ('введите третье число ')
c=int(c)
print (a,'x**2+',b,'x+',c,'=0')
d=((b**2)-(4*a*c))
if d>0 :
    x1=-b+(d**(1/2))
    x2=-b-(d**(1/2))
    print (x1, ';', x2)
elif d==0:
    x=-b/(2*a)
    print (x)
elif d<0:
    print ('уравнение на имеет корней')
else:
    print ('')