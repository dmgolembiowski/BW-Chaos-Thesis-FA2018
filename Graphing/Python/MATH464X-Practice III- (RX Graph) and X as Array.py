
# coding: utf-8

# In[1]:


#Created By Ana Dalipi
#9/17/2018


# In[2]:


import pylab as plt 
import numpy as np 


# In[3]:


r=np.arange(0,4.1,0.0205)# evenly sampled 
x=np.arange(0.5,200
x[0]=0.5

for n in range(1,200):
    z = x[n - 1];#z is previous x
    x[n] = r[n]*z*(1 - z);
    
plt.plot(r,x,'ro')


