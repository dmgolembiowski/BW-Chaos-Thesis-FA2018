#Created By Ana Dalipi
#8/27/2018
#Practice II

import ipywidgets as widgets
from IPython.display import display
import pylab as plt #plots
import numpy as np #mathematical stuff
####INTERACTIVE bby

r=widgets.FloatSlider(min=0.001,max=4.5,value=0,description='Constant:')#add a slider for r values
display(r)

x=range(2000)
x[0]=0.5


def update_plot(r):
    for n in range(1,2000):
        z = x[n - 1];#z is previous x
        x[n] = r*z*(1 - z);#faster when you separate z
    
    plt.plot(x,'ro')
    plt.xlim(1980,2000)#slower but what we need
    #plt.xlim(1,20)#faster
    plt.ylim(-1,1)

widgets.interactive(update_plot,r=r)
