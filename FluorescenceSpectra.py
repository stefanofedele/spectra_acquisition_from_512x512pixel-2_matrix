# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 16:26:34 2016

@author: stefano
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

path = "/home/stefano/Documents/Measurements/Raman/03_10_Angle_resolved_Fluorescence_TMPyP_HClpH1_AuNC_05mWatt/ASCII"
s = '/'
path = path + s
files = os.listdir(path)
files.sort()

j = 0
df = pd.read_csv(path + files[j], sep=',', header = None).astype(float)
df = df.transpose()

fGsize = 2 # First Figure Size
sGsize = 1 # Second Figure Size

wl_id = 120 # wavenumber/wavelength index
pixel_first = 1
pixel_last = 100
mof = df.ix[pixel_first:pixel_last][wl_id].mean() # Mean Out of the Focus
mof_rms = ( np.sum( ( df.ix[pixel_first:pixel_last][wl_id] - mof)**2 ) / (pixel_last - pixel_first) )**0.5 # root mean square of "mof" (Mean Out of the Focus)
#Max_wl = df.ix[pixel_first:][wl_id].max() # max value for wavelength (wl) number wl_id
threshold = mof + 3*mof_rms # threshold = 3 * sigma
upper_value = threshold

jj = pixel_last
while upper_value == threshold:
    if df.ix[jj:][wl_id]> threshold:
        upper_value = df.ix[jj:][wl_id] 
    jj = jj + 1


pixel_first = 0
pixel_last = 511
wl_first = 0
wl_last = 511

fig = plt.figure(figsize=(20,10))
ax1 = plt.subplot2grid((fGsize,sGsize), (0,0), rowspan=fGsize - 1) # first braket is the figure size, the second one is the on-going plot position
#plt.axis([wl_first, wl_last, Min, Max])    

line1, = ax1.plot(df.ix[1:][wl_id])
#line1, = ax1.plot(wl_shift, spectrum, label = files[k][6:15])    
##fucking legend!
#handles, labels = ax1.get_legend_handles_labels() # http://matplotlib.org/1.3.1/users/legend_guide.html
#ax1.legend(handles[::-1], labels[::-1])
# plt.plot(x, y, label = "plot label") # the easiest way to get a legend
# plt.legend()
#fucking legend!
ax1.grid()
ax2 = plt.subplot2grid((fGsize,sGsize), (fGsize - 1,0), rowspan=1)
ax2.imshow(df.ix[:][pixel_first:pixel_last], cmap=cm.gray, extent=[wl_first,wl_last,pixel_last,pixel_first])