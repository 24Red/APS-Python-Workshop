#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created for APS Summer REU Python 3 Workshop

@author: victoriacatlett
"""

###############################################################################
############# Import what you need from packages at the top ###################
###############################################################################

import numpy as np
import matplotlib.pyplot as plt


###############################################################################
########### TASK 1: Calculate y = 3x^2 +2x + 1 on the given x values ##########
###############################################################################

my_x = np.linspace(-10, 10, 50)

def quadratic(x):
    ### YOUR CODE HERE ###

my_y = quadratic(my_x)

###############################################################################
### TASK 2: Plot x and y values with green triangles. Include Legend label ####
###############################################################################

plt.figure()

# YOUR CODE HERE: Plot the data from the last cell (my_x and my_y)

plt.xlabel('x')
plt.ylabel(r'$y = x^{2}$')
plt.title('This is a plot!')
plt.legend()
plt.show()

# This line saves your plot as a PNG in the "files" folder
fig.savefig('../../files/Sample_Plot.png')