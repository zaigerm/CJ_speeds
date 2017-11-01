#!/usr/bin/env python
'''this code is for initial calculation and comparison of enthalpy matched detonation speeds '''

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
import os
#matplotlib.use('TKAgg') #this supresses the ploting on the terminal 


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
def get_gamma(p,T,species,mech):
	import cantera as ct
	gas = ct.Solution(mech)
	gas.TPX = T,p,species
	gamma = gas.cp/gas.cv
	return gamma
	


p =101325
T = 300
N2_dilution = []
CO2_dilution = []
cj_n2 = []
cj_co2 = []
gamma_n2 = []
gamma_co2 = []
dilution_range = np.arange(0.0,0.6,0.05)
#print len(dilution_range)
mech = 'CSMmech7_2.cti'
for i in dilution_range:
	N2_dilution.append('C3H8:1 N2O:10 N2:'+str(i))
	CO2_dilution.append('C3H8:1 N2O:10 CO2:'+str(i))

#print len(N2_dilution)


if __name__ == '__main__':
	for it in xrange(len(dilution_range)):
		gamma_n2.append(get_gamma(p,T,N2_dilution[it],mech))
		gamma_co2.append(get_gamma(p,T,CO2_dilution[it],mech))
	print gamma_n2
	print gamma_co2
	#a = get_cj(p, T, N2_dilution, mech)
	#print cj_co2
	#for bleh in xrange(len(dilution_range)):
	#	blockPrint()
	#	cj_n2.append(get_cj(p,T,N2_dilution[bleh],mech))
	#	cj_co2.append(get_cj(p,T,CO2_dilution[bleh],mech))
	#	enablePrint()
	
#plt = matplotlib.pyplot
	
	#fig = plt.figure(num =None, figsize = (8,6), dpi = 600)
	#plt.plot(dilution_range*.95,cj_co2)
	#plt.plot(dilution_range,cj_n2, '--')
#plt.plot(values['x'], values['p'], 'k')
	#plt.legend((r'$CO_{2}$',r'$N_{2}$'))
	#plt.title("CJ Detonation Comparison")
	#plt.xlabel(r'$Y_{N_{2}}$ Equivalent', fontsize=14)
	#plt.ylabel('Velocity [m/s]',fontsize=14)
#plt.show()
	#plt.savefig('cj_speeds.png')
#for i in xrange(len(self.species)):
#string_list.append(self.species[i] + ':' + str(self.concentration[i,x,y]))
#gas.X = ', '.join(string_list)
