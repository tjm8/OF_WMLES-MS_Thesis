import numpy as np
import matplotlib.pyplot as plt

rho = 1; v = 56.0; A = 0.012

#t='0'
t_stamp='0.0216'
t_stamp='0.0576'

dat = np.loadtxt('../postProcessing/probes/'+t_stamp+'/p',skiprows=13)
t=dat[:,0]
p=dat[:,8]
plt.plot(p)

t=dat[:,0]
p=dat[:,11]
plt.plot(p)

plt.show()


