#Created By Ana Dalipi
#8/27/2018
#Practice I

import pylab as plt #plots
import numpy as np #mathematical stuff


r=0.9
x=range(200)
x[0]=0.5
for n in range(1,200):
    z = x[n - 1];#z is previous x
    x[n] = r*z*(1 - z);
    #print(x[n])#print results; all points
    
plt.plot(x,'ro')
###############
r=1.1
x=range(2000)
x[0]=0.5
for n in range(1,2000):
    z = x[n - 1];#z is previous x
    x[n] = r*z*(1 - z);
    #print(x[n])#print results; all points
    
plt.plot(x,'ro')
#################
r=3.84
x=range(200)
x[0]=0.5
for n in range(1,200):
    z = x[n - 1];#z is previous x
    x[n] = r*z*(1 - z);
    #print(x[n])#print results; all points
    

plt.plot(x,'ro')
plt.xlim(189,200)#scale n onx-axis
plt.ylim(0,1)#scale on y-axis
##############
r=3.4
x=range(2000)
x[0]=0.5
for n in range(1,2000):
    z = x[n - 1];#z is previous x
    x[n] = r*z*(1 - z);
    #print(x[n])#print results; all points
    

plt.plot(x,'ro')
plt.xlim(1989,2000)#scale n on the x-axis
