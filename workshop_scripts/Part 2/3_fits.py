#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created for APS Summer REU Python 3 Workshop

@author: victoriacatlett
"""

###############################################################################
############# Import what you need from packages at the top ###################
###############################################################################

import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.visualization import make_lupton_rgb


###############################################################################
##### Open "combined.fits" (in the "files" folder) and see what's inside ######
###############################################################################

allData = fits.open('../../files/CassiopeiaA.fits')
print(allData.info())


###############################################################################
###### Import each of the three images as red, green, and blue channels #######
###############################################################################

# Access the individual images and headers from allData
r1 = allData[0].data
rHeader1 = allData[0].header

g1 = allData[1].data
gHeader1 = allData[1].header

b1 = allData[2].data
bHeader1 = allData[2].header

# Another way: Open them directly from the file
# r1, rHeader1 = fits.getdata('../files/CassiopeiaA.fits', 0, header=True)
# g1, gHeader1 = fits.getdata('../files/CassiopeiaA.fits', 1, header=True)
# b1, bHeader1 = fits.getdata('../files/CassiopeiaA.fits', 2, header=True)


###############################################################################
################ TASK 1: Get information about the first image ################
###############################################################################

# YOUR CODE HERE

###############################################################################
############### TASK 2: Plot red channel, then save the image #################
###############################################################################

plt.figure()

# YOUR CODE HERE: 
# Plot the image
# Include these kwargs: origin='lower', cmap='gray'




# Adding some information to the plot
plt.colorbar()
plt.title('0.5-1.5 keV Data of Cassiopeia A from Chandra X-Ray Telescope')

# YOUR CODE HERE:
# Save the figure as an image




###############################################################################
############# HELPFUL EXAMPLE: Make RGB Image from the 3 channels #############
###############################################################################

plt.figure()
image = make_lupton_rgb(r1, g1, b1, stretch=50)
plt.imshow(image, origin = 'lower')
plt.title('3-filter Image of Cassiopeia A from Chandra X-Ray Data')
plt.savefig('../files/CassiopeiaA.png')