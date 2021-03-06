#Created By Ana Dalipi
#9/13/2018
#Using Bookeh for a much more interactive plot to pinpoint and zoom where divergence happens

import pylab as plt #plots
import numpy as np #mathematical stuff
from bokeh.plotting import figure, output_notebook, show
from bokeh.models import HoverTool, BoxZoomTool, PanTool, WheelZoomTool


output_notebook()#for jupyter notebook only
plot1 = figure(plot_width=900, plot_height=700,x_range=(1980,2000))#looking at last 20 values

# Set up data
x=np.arange(0.5,2000)
r=0.5

for n in range(1,2000):
    z = x[n - 1];#z is previous x
    x[n] = r*z*(1 - z);
    #print(x[n])#print results; all points

plot1.circle(range(2000),x,color="green", size=10)
show(plot1)

############Next Value of R
plot2 = figure(plot_width=900, plot_height=700,x_range=(1980,2000))#new plot

x=np.arange(0.5,2000)
r=2.99

for n in range(1,2000):
    z = x[n - 1];#z is previous x
    x[n] = r*z*(1 - z);
    #print(x[n])#print results; all points

plot2.circle(range(2000),x,color="green", size=10)
show(plot2)
