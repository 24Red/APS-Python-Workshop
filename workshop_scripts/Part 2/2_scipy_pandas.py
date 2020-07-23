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
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

###############################################################################
################### Define a function we'll need later ########################
###############################################################################

def mySin(x,a,b):
    y = a*np.sin(b*x)
    return y


###############################################################################
############# TASK 1: Read in the Excel file OR the CSV file ##################
###############################################################################

path_to_xlsx = '../../files/pandas.xlsx'
#path_to_csv = '../../files/pandas.csv'

data = # YOUR CODE HERE: Read in the data
x =    # YOUR CODE HERE: Get the x data
y =    # YOUR CODE HERE: Get the y data


###############################################################################
################# TASK 2: Plot data (BONUS: Plot fit sine) ####################
###############################################################################

# This creates two places to plot (ax[0] and ax[1])
# on a single figure called "fig"
fig, ax = plt.subplots(nrows=2, ncols=1)
plt.subplots_adjust(hspace=0.5)

# Set titles for the two plots
ax[0].set_title('Original Data')
ax[1].set_title('Fit Sine Curve')

# YOUR CODE HERE:
# Plot the data as black points on the top plot (ax[0])
# Hint: You'll plot using ax[0].something, not plt.something 



### BONUS SECTION:
# This code is finding "a" and "b" of the sine curve that 
# best fits the data points
parameters, cov = curve_fit(mySin, x, y, p0=[1, 6])
a_fit = parameters[0]
b_fit = parameters[1]

# YOUR CODE HERE: 
# Find the y-values of the sine (mySin) function where 
# x = the x's from the data, a=a_fit, and b=b_fit.
# Name the list of y-values "y_fit"



# YOUR CODE HERE:
# Plot the best-fit function as a black line



# This will just show you how the fit values compare to the true
# values I used when making the sample data
print('The fit found y = %0.2f*sin(%0.2f*x)'%(a_fit,b_fit))
print('The real answer is y = 0.75*sin(2*pi*x)')
print(cov)

###############################################################################
##################### TASK 3: Save new data to a file #########################
###############################################################################

# y_fit = np.zeros(len(x))  # UNCOMMENT if you couldn't get Task 2 bonus

# This adds a NEW column to the ORIGINAL dataframe
# then saves the data as Excel sheet
data['y_fit'] = y_fit
data.to_excel('../../files/pandas_fit.xlsx', index=False)

# This creates a NEW dataframe entirely
saveData = pd.DataFrame({'x':x, 'y':y, 'y_fit':y_fit})

# YOUR CODE HERE:
# Save saveData to a CSV in the "files" folder


