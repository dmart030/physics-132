# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:10:11 2015

@author: Lalecia
"""
import numpy as np
import matplotlib.pyplot as plt
y =np.array([109, 104, 100, 97.2, 81.6, 76])
m =np.array([109, 104, 100])
m1 = np.array([81.6,76,70])
b1 = np.array([19, -4, -11])
b =np.array([55.7, 48.7, 45.7])
x =np.array([55.7, 48.7, 45.7, 23, 0, -8])
coefficients = np.polyfit(x, y, 1)
coefficients1 = np.polyfit(m,b, 1)
coefficients2 = np.polyfit(m1,b1,1)
polynomial = np.poly1d(coefficients)
polynomial1 = np.poly1d(coefficients1)
polynomial2 = np.poly1d(coefficients2)
ys2 = polynomial2(x)
ys1 = polynomial1(x)
print coefficients1, "coefficients of first graph."
print polynomial1, "polynomial equation of first graph."
print coefficients2, "coefficients of the second graph."
print polynomial2, "coefficients of the second graph."
ys = polynomial(x)
print coefficients,"cofficients of total graph"
print polynomial, "Polynomials of total graph"

plt.plot(x, y, 'o')

plt.plot(x, ys)
plt.ylabel('Pressure[Pa]')
plt.xlabel('Temperature[C]')
plt.xlim(-10,60)
plt.ylim(60,110)
plt.show()
plt.savefig('plot.jpeg')
plt.plot(m,b, 'o')
plt.ylabel('Pressure[Pa]')
plt.xlabel('Temperature[C]')
plt.xlim(-10,60)
plt.ylim(60,110)
plt.show()
plt.plot(m1,b1,'o')
plt.plot(m,ys1)
plt.ylabel('Pressure[Pa]')
plt.xlabel('Temperature[C]')
plt.xlim(-10,60)
plt.ylim(60,110)
plt.show()