from sympy import symbols
from sympy.vector import CoordSys3D
from sympy import sin, acos, trigsimp
import math
N = CoordSys3D('N')
a, b, c = symbols ('a, b, c')


a = 4*N.i + 3*N.j + 8*N.k
b = -2*N.i + 8*N.j + 7*N.k
c = -5*N.i - 6*N.j + 12*N.k

S = a.dot(b)
V = a.dot(c)
P = b.dot(c)

am = a.magnitude()
bm = b.magnitude()
cm = c.magnitude()

r1 = S/(am*bm)
x=acos(r1)

r2 =V/(am*cm)
y=acos(r2)

r3 =P/(bm*cm)
z=acos(r3)


print( math.degrees( x.evalf() ) )
print( math.degrees( y.evalf() ) )
print( math.degrees( z.evalf() ) )