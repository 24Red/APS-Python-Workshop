#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created for APS Summer REU Python 3 Workshop

@author: victoriacatlett
"""

###############################################################################

# This example will use pi and sin() from NumPy to evaluate sin(pi/2)

import numpy as np

print(np.sin(np.pi/2))

###############################################################################

# Task) Find the values of sin(0) and sin(pi). What happens?
#
#       Write your code below


###############################################################################

import matplotlib.pyplot as plt

sample_x = [1, 2, 3, 4, 5]
sample_y = [1, 4, 9, 16, 25]

# Plotting sample_x vs sample_y as red triangles
# "label = " sets a label for the legend
plt.figure()
plt.scatter(sample_x, sample_y, color = 'red', marker = 'v', label='My data')

# Add x- and y-axis labels
plt.xlabel('The x axis')
plt.ylabel('The y axis')

# Add a title
plt.title('The Title')

# Add a legend
plt.legend()

###############################################################################

import pandas as pd

# Go back 2 folders, into the "files" folder, and identify Excel sheet
path2data = '../../files/sample_data.xlsx'

# Use pandas to load the Excel data
data = pd.read_excel(path2data)

# Make the Excel column called "x" be the x-values for our plot
x = data['x']      # or x = data.x

# Make the Excel column called "sin_x" be the y-values for our plot
y = data['sin_x']  # or y = data.sin_x

# Plot the data
plt.figure()
plt.plot(x,y)

###############################################################################

from scipy.stats import norm

mu = 1
sigma = 2

# Create 100 equally-spaced numbers between -5 and 5
x = np.linspace(-5,5,100)

# Evaluate a Gaussian at those 100 x values
y = norm.pdf(x,mu,sigma)

# Plot the resulting Gaussian
plt.figure()
plt.plot(x,y)

# Add a title with math symbols
plt.title(r'Gaussian with $\mu$ = %i and $\sigma$ = %i'%(mu,sigma))

###############################################################################