# For output ASIC readout from GAPS database
# Author: Jiancheng Zeng
# Date: Dec 17th, 2023


import os
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from sqlalchemy import create_engine
import warnings
warnings.filterwarnings('ignore')
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
from matplotlib.pyplot import figure


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

'''
construct plotted modules
'''
T_ORI=[]
T_ORI.extend(T[0].reshape(-1))
x=[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]
y=[0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
z=[10]*36
for i in range(6):
    x.extend([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5])
    y.extend([0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5])
    z.extend([9-i]*36)
    T_ORI.extend(T[i+1].reshape(-1))

colmap = cm.ScalarMappable(cmap=cm.winter)
colmap.set_array([-40, -15])

# reference for cmap. note cmap and c are different!
# http://matplotlib.org/examples/color/colormaps_reference.html
ax.scatter(x, y, z, marker='s',s = 200, alpha = 0.9, c=T_ORI, cmap='winter', vmin = -40, vmax = -15);
cb = fig.colorbar(colmap, cax=fig.add_axes([0.9, 0.1, 0.03, 0.8]), label='\N{DEGREE SIGN}C')

ax.set_zlim(0, 10)
ax.set_xlabel('BOM side');
ax.set_ylabel('Sun panel side');
ax.set_zlabel('vertical direction');
ax.set_title('Original tracker temperature');
ax.set_zticks([])

plt.show()
# change view angle 
# http://infamousheelfilcher.blogspot.com/2013/02/changing-viewing-angle-of-matplotlib.html
#ax.view_init(azim = 0,elev = 0)

