import numpy as np


dat1 = np.loadtxt("u_clean0.0258.dat")
print(dat1.shape)

dat2 = np.loadtxt("u_clean0.129.dat")
print(dat2.shape)


dat = np.append(dat1,dat2,axis=0)
print(dat.shape)

np.savetxt('u_clean_all', dat)


