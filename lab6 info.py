# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:05:51 2015

@author: D
"""
import numpy as np
import matplotlib.pyplot as plt
T_cChrome = np.array([63.7, 49.9, 33.8, 18.6, 4.2])
T_HChrome = np.array([77.0, 65.7, 52.5, 34.6, 21.4 ])
T_FChrome = np.array([59.7, 47.6, 31.6, 18.2, 3.1 ])
M_H2OChrome = np.array([100.00,106.00,113.30,92.43,53.7])

T_cCu = np.array([60.0, 50.0, 34.7, 21.0, 5.0])
T_HCu = np.array([77.0, 65.7, 48.6, 35.0, 21.0])
T_FCu = np.array([61.2, 52.1, 34.7, 21.0, 7.3])
M_H2OCu = np.array([100.00, 106.00, 113.30, 92.43, 53.7])
R = 8.314
DulongC_v = np.array([3*R for i in range(10)])
x = np.array([i for i in range(10)])


cv_einChrome = 3*R*((T_FChrome/T_HChrome)**2)*(np.e**(T_FChrome/T_HChrome))
cv_einChrome /= ((np.e**(T_FChrome/T_HChrome))-1)**2
cv_deb = 12*((np.pi)**4)**.5*R*(T_HChrome**3)/(T_FChrome**3)
plt.plot(x, DulongC_v, cv_einChrome, cv_deb, '-')

plt.show()