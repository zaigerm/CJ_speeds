#!/usr/bin/env python
'''this code is for initial calculation and comparison of enthalpy matched detonation speeds '''

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
import os
matplotlib.use('TKAgg') #this supresses the ploting on the terminal 


# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

def get_cj(p,T,species,mech):
	from SDToolbox import *
	[cj,_] = CJspeed(p,T,species,mech,0)
	return cj


p =101325
T = 300
N2_dilution = []
CO2_dilution = []
cj_n2 = []
cj_co2 = []
dilution_range = np.arange(0.0,0.1,0.05)
#print len(dilution_range)
mech = 'CSMmech7_2.cti'
for i in dilution_range:
	N2_dilution.append('C3H8:1 N2O:10 N2:'+str(i))
	CO2_dilution.append('C3H8:1 N2O:10 CO2:'+str(i))

#print N2_dilution[0]
for bleh in xrange(len(dilution_range)):
	blockPrint()
	cj_n2 = get_cj(p,T,N2_dilution[bleh],mech)
	cj_co2 = get_cj(p,T,CO2_dilution[bleh],mech)
	enablePrint()

#plt = matplotlib.pyplot

fig = plt.figure()
plt.plot(dilution_range,cj_co2)
plt.plot(dilution_range,cj_n2)
plt.savefig('cj_speeds.png')
#for i in xrange(len(self.species)):
#string_list.append(self.species[i] + ':' + str(self.concentration[i,x,y]))
#gas.X = ', '.join(string_list)

if __name__ == '__main__':
	#a = get_cj(p, T, N2_dilution, mech)
	print cj_co2