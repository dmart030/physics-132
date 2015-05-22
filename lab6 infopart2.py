import numpy as np
import matplotlib.pyplot as plt
T_cChrome = np.array([63.7, 49.9, 33.8, 18.6, 4.2,-10.0,-25.,-40.,-55.,-75.])
T_HChrome = np.array([77.0, 65.7, 52.5, 34.6, 21.4, 5., -10.11, -24.12, -40., -55.7 ])
T_FChrome = np.array([59.7, 47.6, 31.6, 18.2, 3.1,-7.3, -24.41,-41.05,-54.45,-75.45 ])
M_H2OChrome = np.array([100.00,106.00,113.30,92.43,53.7])

T_cCu = np.array([60.0, 50.0, 34.7, 21.0, 5.0, -9.8, -25.4, -41.05, -54.45, -74.48])
T_HCu = np.array([77.0, 65.7, 48.6, 35.0, 21.0, 5.0, -10.2, -22.5, -42.3, -55.2])
T_FCu = np.array([61.2, 52.1, 34.7, 21.0, 7.3, -7.3, -24.41, -41.05, -54.45, -74.48])
M_H2OCu = np.array([100.00, 106.00, 113.30, 92.43, 53.7])
R = 8.314
DulongC_v = np.array([3*R for i in range(10)])
x = np.array([i for i in range(10)])

cv_chrome=(12*((np.pi)**4)/5)*R*(T_cChrome**3)/(T_FChrome**3)
cv_Cu=(12*((np.pi)**4)/5)*R*(T_cCu**3)/(T_FCu**3)
cv_chrome *= 0.01
cv_Cu *=0.01
plt.plot(x,cv_chrome,label='Cv debye chromium')
plt.plot(x,DulongC_v,label='Cv Dulong')
plt.plot(x,cv_Cu,label='Cv debye Cu')
plt.title('graph of the Cv Dulong vs Cv Debye')
plt.legend()
plt.show()
plt.savefig('chromium_debye&cudebye.jpg')
