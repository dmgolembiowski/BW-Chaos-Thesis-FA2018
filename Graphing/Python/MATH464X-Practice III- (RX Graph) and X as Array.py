
# coding: utf-8

# In[1]:


#Created By Ana Dalipi
#9/17/2018


# In[2]:


import pylab as plt 
import numpy as np 


# In[3]:


r=np.arange(0,4.1,0.0205)# evenly sampled 
x=range(200)
x[0]=0.5

for n in range(1,200):
    z = x[n - 1];#z is previous x
    x[n] = r[n]*z*(1 - z);
    
plt.plot(r,x,'ro')


# In[4]:


#Testing values of X
print x[189]



# In[5]:


print x[0]


# In[6]:


print x[2]


# In[7]:


print x



# In[8]:


print (x[2].shape)#shape
print (x[1].shape)
x[199].shape


# In[9]:


print x[1].ndim#dimension
print x[1].size#size


# In[10]:


r=np.arange(0,4.1,0.0205)# evenly sampled 
x=range(200)#This is a list
x[0]=0.5

print x
print r



# In[11]:


for n in range(1,200):
    z = x[n - 1];#z is previous x
    x[n] = r[n]*z*(1 - z);
    print x[n]
    print x[n].size
    


# In[12]:


print x


# In[13]:


r=np.arange(0,4.1,0.0205)# evenly sampled 
x=np.arange(0.5,200)#this makes it an array


for n in range(1,200):
    z = x[n - 1];#z is previous x
    x[n] = r[n]*z*(1 - z);
    print x[n].size


# In[14]:


print x[0]


# In[15]:


print x[1]


# In[16]:


print x


# In[17]:


x.size


# In[18]:


print x[189]


# In[19]:


print x[70]


# In[20]:


r=np.arange(0,4.1,0.0205)# evenly sampled 
x=x=np.arange(0.5,200)#this makes it an array


for n in range(1,200):
    z = x[n - 1];#z is previous x
    x[n] = r[n]*z*(1 - z);
    
plt.plot(r,x,'ro')


# In[21]:


r=3.9
x=x=np.arange(0.5,200)#this makes it an array

for n in range(1,200):
    z = x[n - 1];#z is previous x
    x[n] = r*z*(1 - z);
    #print x[n].size
    
  
    

plt.plot(x,'ro')
plt.xlim(189,200)#scale n
plt.ylim(0,1)


# In[22]:


#########BOOkeh--->Has Problems
from bokeh.plotting import figure, output_notebook, show
from bokeh.models import HoverTool, BoxZoomTool, PanTool, WheelZoomTool
import sys


# In[23]:


output_notebook()
plot = figure(plot_width=400, plot_height=400)


# In[24]:


plot = figure(plot_width=900, plot_height=700,x_range=(0,4),y_range=(0,1))


# In[25]:


x=range(200)
x[0]=0.5
r=np.arange(0,4.1,0.0205)

for n in range(1,200):
    z = x[n - 1];#z is previous x
    x[n] = r*z*(1 - z);
   



# In[81]:



plot.circle(r,x,color="green", size=10)
show(plot)

