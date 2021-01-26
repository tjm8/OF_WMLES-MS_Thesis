import numpy as np
import matplotlib.pyplot as plt

rho = 1; v = 56.0; A = 0.012

#t='0'
t='0.057625'


Fv = np.loadtxt('force_mon'+t+'/Fvx') /(1/2*rho*v**2*A)
Fp = np.loadtxt('force_mon'+t+'/Fy_tot') /(1/2*rho*v**2*A)
Fpx = np.loadtxt('force_mon'+t+'/Fpx') /(1/2*rho*v**2*A)

fig,cf_ax = plt.subplots()
cf_ax.plot(Fv)
plt.ylabel('Cdf',fontsize=16)
#plt.ylim((0.0085,0.01))
plt.grid()

fig,cp_ax=plt.subplots()
cp_ax.plot(Fp)
plt.ylabel('Cl',fontsize=16)
#plt.ylim((0.7,0.76))
plt.grid()

fig,cd_ax=plt.subplots()
cd_ax.plot(Fpx)
plt.ylabel('Cd',fontsize=16)
#plt.ylim((0.7,0.76))
plt.grid()


t = '0.086225'
Fv = np.loadtxt('force_mon'+t+'/Fvx') /(1/2*rho*v**2*A)
cf_ax.plot(Fv)
Fp = np.loadtxt('force_mon'+t+'/Fy_tot') /(1/2*rho*v**2*A)
cp_ax.plot(Fp)
Fpx = np.loadtxt('force_mon'+t+'/Fpx') /(1/2*rho*v**2*A)
cd_ax.plot(Fpx)






plt.show()
