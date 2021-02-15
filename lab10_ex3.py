import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(-5, 5, 0.01)
	
def diff_func(z, t):
    y, w = z 
    dy_dt = w
    dw_dt = np.sin(t)+np.cos(t)
    return dy_dt, dw_dt
y0 = 3
dy0 = 0
z0 = y0, dy0

sol = odeint(diff_func, z0, t)
plt.plot(t, sol[:, 1], 'b', label='theta(t)')
plt.plot(sol[:, 1], sol[:, 0], 'g', label='theta(omega)')
plt.plot(sol[:, 0], sol[:, 1], 'g', label='omega(theta)')
plt.legend()
plt.show()