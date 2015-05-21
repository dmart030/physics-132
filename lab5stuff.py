# -*- coding: utf-8 -*-
"""
Created on Thu May 07 19:16:53 2015

@author: Dominic Martinez-Ta
"""
import numpy as np
Ti = np.array([7.8, 10.7, 13.7, 15.1, 4.9, 7.8, 8.8])
Tf = np.array([8.8, 12.7, 14.2, 15.6, 7.8, 8.8, 10.3])
T = np.array([46.4, 41.5, 38.6, 37.1, 44.9, 43.5, 39.6])
s = np.array(['Iron', 'copper', 'teflon', 'lead', 'Aluminium', 'chromium', 'rock'])
total_stuff = np.array([s,Ti,Tf,T])
print "substrates", s
print "initial temperatures", Ti
print "Final Temperatures", Tf
print "Resevoir Temperatures", T
print '\n'

#=-----------------------------------------
#ethanol and dry ice

#calculating latent heat

s2 = np.array(['Al', 'Cu', 'tefflon', 'chromium[6 pieces]', 'rock'])
Tc = np.array([-72.3, -73.3, -73.2, -72.8, -73.7, -71.3])
Th = np.array([49.5, 61.5, 54.2, 49.8, 54.4, 40.0,])
dx = np.array([1.83, 2.05, 2.90, 1.9, 1.2, 3.9])
print "substrates", s2
print "Cold temperatures", Tc
print "Hot Temperatures", Th
print "Change in heat", dx

I = 2.22 #Amps
V = 5.44 #volts
P =I*V
