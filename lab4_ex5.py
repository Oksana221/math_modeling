import math

def k(a):
    x=math.pi*(a**2)
    return x

def p(a, b):
    x=a*b
    return x

def t(a, b, c):
    h=(a+b+c)/2
    x=math.sqrt((h*(h-a)*(h-b)*(h-c)))
    return x

print('1 круг')
print('2 прямоугольник')
print('3 треугольник')
m=int(input('выберите фигуру'))
    
if m==1:
    a=float(input('введите радиус a='))
    
    print(k(a))
    
elif m==2:
    a=float(input('введите сторону a='))
    b=float(input('введите стoрону b='))
    print(p(a, b))
elif m==3:
    a=float(input('введите сторону a='))
    b=float(input('введите стoрону b='))
    c=float(input('введите сторону c='))
    print(t(a, b, c))