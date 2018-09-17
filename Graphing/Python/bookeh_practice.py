#Created By Ana Dalipi
#9/13/2018
#Using Bookeh for a much more interactive plot

import pylab as plt #plots
import numpy as np #mathematical stuff
from bokeh.plotting import figure, output_notebook, show
from bokeh.models.sources import ColumnDataSource
from bokeh.models import HoverTool, BoxZoomTool, PanTool, WheelZoomTool
from bokeh.models import Range1d, Range

output_notebook()#for jupyter notebook only
plot1 = figure(plot_width=900, plot_height=700,x_range=(1980,2000))#looking at last 20 values

# Set up data
x=range(2000)
x[0]=0.5
r=0.5

for n in range(1,2000):
    z = x[n - 1];#z is previous x
    x[n] = r*z*(1 - z);
    #print(x[n])#print results; all points

plot1.circle(range(2000),x,color="green", size=10)
show(plot1)

############Next Value of Graph
plot2 = figure(plot_width=900, plot_height=700,x_range=(1980,2000))#new plot

x=range(2000)
x[0]=0.5
r=2.99

for n in range(1,2000):
    z = x[n - 1];#z is previous x
    x[n] = r*z*(1 - z);
    #print(x[n])#print results; all points

plot2.circle(range(2000),x,color="green", size=10)
show(plot2)
