#!/usr/bin/env python3
from matplotlib.widgets import Cursor
from matplotlib.transforms import offset_copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtrans
import mplcursors

nValue = []
XnValue = []
lastN = []
lastXn = []
xs = np.arange(300)
ys = np.arange(300)
def logistic(r, x, num_Terms):
    n = 0
    nFile = str(num_Terms) + ".txt"
    xFile = str(r) + ".txt"

    while n < num_Terms:
        nValue.append(n)
        with open(nFile, 'wt') as w:
            w.write(str(n)+",")
        XnValue.append(x)
        with open(xFile, 'wt') as W:
            W.write(str(x) + ",")
        if n >= num_Terms - 10:
            lastNTerms(n)
            lastXnTerms(x)
            xs[n] = n
            ys[n] = x
            print(xs[n],ys[n])
        x = r * x * (1.0 - x)
        print(x)
        n += 1
    #print(nValue)
    #print(XnValue)
    return nFile, xFile

def lastNTerms(nt):
    lastN.append(nt)

def lastXnTerms(xt):
    lastXn.append(xt)

rValue = input('Enter r value: ')
rValue = float(rValue)

xValue = input('Enter x0 value: ')
xValue = float(xValue)

nTerms = input('Generate 300 terms? [y/n]:  ')
if nTerms != 'y':
    nTerms = input('Enter the number of terms to generate: ')
    nTerms = int(nTerms)
else:
    nTerms = 300
readN, readX = logistic(rValue, xValue, nTerms)
print('Use file: ', readN)
print('Use file: ', readX)

# Next get the last 50 terms using
# lastN and lastXn
fig = plt.figure(figsize=(8,6 ))
ax = fig.add_subplot(111, facecolor='#FFFFCC')
nIter = 0
"""
while nIter <= nTerms:
    #nAxis = lastN[nIter]
    #xAxis = lastXn[nIter]
    print('nAxis=nValue[nIter]=',nValue[nIter],'nIter=', nIter,'nTerms=', nTerms)
    nAxis = nValue[nIter]
    xAxis = XnValue[nIter]
    ax.plot(nAxis, xAxis, 'o')
    nIter += 1
#ax.set_xlim(0, nTerms)
ax.set_xlim(nTerms - 50, nTerms)
ax.set_ylim(-0.25, max(XnValue) + 0.25)
"""
# set useblit = True on gtkagg for enhanced performance
cursor = Cursor(ax, useblit=True, color='blue', linewidth=0.5)
mplcursors.cursor(hover=True)
plt.show()
"""
fig = plt.figure(figsize=(5,10))
axis = plt.subplot(2, 1, 2, projection='polar')
trans_offset = mtrans.offset_copy(axis.transData, fig=fig, y=300, units='dots')

for z, w in zip(xs, ys):
    plt.polar((z,), (w,), 'ro')

plt.show()
"""