a=input('введите первый член ')
a=int(a)
b=input('введите знаменатель ')
b=int(b)
c=input('введите количество членов прогрессии ')
c=int(c)
for n in range(1, c+1, 1):
    print(a*b**(n-1))
    