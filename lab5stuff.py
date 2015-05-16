# -*- coding: utf-8 -*-
"""
Created on Thu May 07 19:16:53 2015

@author: Dominic Martinez-Ta
"""
import numpy as np
objects = ['iron','Cu','Tefflon','lead','Al','Chromium','rock']
M = np.array([49.86, 40.00, 8.55, 44.71, 14.96, 7.51, 13.62])
ti = np.array([7.8, 10.7, 13.7, 15.1, 4.9, 7.8, 8.8])
tf = np.array([8.8, 12.7, 14.2, 15.6, 7.8, 8.8, 10.3])
T1 = np.array([46.4, 41.5, 38.6, 37.1, 44.9, 43.5, 39.6])


#=-----------------------------------------
#ethanol and dry ice

#calculating latent heat
objects = ['iron','Cu','Tefflon','lead','Al','Chromium','rock']
t = np.array([60 for i in range(len(objects))])
T2 = np.array([49.8, 61.5, 49.8, 54.2, 50.0, 45.4, 40.0])
Tcold = np.array([-72.3, -73.2, -72.8, -73.2, -72.3, -73.7, -71.3])
dx = np.array([4.2, 2.05, 1.9, 2.90, 1.83, 1.20, 3.9])


I = 2.22 #A
V = 5.44 #V
P =I*V