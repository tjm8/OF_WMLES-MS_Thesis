import numpy as np
import matplotlib.pyplot as plt

ipt = int(1);
fig, ax = plt.subplots()


p = np.loadtxt('res/pres')
ax.plot(p[0::int(2*ipt)] ,label='pressure correction' )

ux = np.loadtxt('res/uxres')
ax.plot(ux[0::ipt],label='Ux' )

uy = np.loadtxt('res/uyres')
ax.plot(uy[0::ipt] ,label ='Uy' )


ax.legend()
plt.yscale('log')

plt.grid()

plt.show()
