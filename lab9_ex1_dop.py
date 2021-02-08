import numpy as np
from scipy.integrate import odeint 
import matplotlib.pyplot as plt
G = 6.6743015*10**(-11)
M = 5.97*10**24
R = 6371000
h = 300000
x = np.arange(0, h, 100)
def met (v, x):
    dvdx = (G*M)/(v*((h+R-x)**2))
    return dvdx

solve_Bi = odeint(met, 0.000001, x)
plt.plot(x, solve_Bi[:,0], label='изменение скорости')
plt.xlabel('x')
plt.ylabel('v')
plt.title('изменение скорости')
plt.legend()

plt.show()