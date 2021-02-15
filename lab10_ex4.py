import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(-5, 5, 0.01)
	
def diff_func(z, t):
    y, w = z 
    dy_dt = w
    dw_dt = -4*w-5*y
    return dy_dt, dw_dt
y0 = 4
dy0dt = -1
z0 = y0, dy0dt

sol = odeint(diff_func, z0, t)
plt.plot(t, sol[:, 1], 'b', label='theta(t)')
plt.plot(sol[:, 1], sol[:, 0], 'g', label='theta(omega)')
plt.plot(sol[:, 0], sol[:, 1], 'g', label='omega(theta)')
plt.legend()
plt.show()