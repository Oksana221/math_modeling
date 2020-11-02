def h(a, b):
    if b==0:
        return 1
    x=a
    for i in range(1, abs(b), 1):
        x=x*a
    if b<0:
        return 1/x
   
    return x

a=int(input('введите действительное положительное число'))
b=int(input('введите целое число'))
print(h(a, b))
