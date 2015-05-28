# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:56:57 2015

@author: owner
"""

import numpy as np
import matplotlib.pyplot as plt

DataIN = np.loadtxt('3642 8432x 3298y PL 600 T2 D1 100x.txt')
y = []
v = []
for column in DataIN:
    v.append(column[1])
    y.append(column[0])
plt.plot(y,v, 'b')
plt.ylabel('Intensity')
plt.title('PL Spectra')
plt.xlabel('Energy [eV]')
plt.savefig('3298PL.jpg')