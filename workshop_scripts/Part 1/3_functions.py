#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created for APS Summer REU Python 3 Workshop

@author: victoriacatlett
"""

###############################################################################

# Task) Determine what kind of variable you get when you 
#       divide 18 by 3 (both integers). 
#
#       Write your code below





# Is the result the type of variable you expected?

###############################################################################

# Task) Find the sum of the minimum and maximum of [1,2,3,4]
#
#       Write your code below





###############################################################################

# Task) Determine if the following statement is True or False:
#       not (20 is less than or equal to 19)
#
#       Write your code below




###############################################################################

'''
A while loop is constructed like this:

while condition:
    # stuff to do
    
Be careful, or you might accidentally make a loop that will go on forever!
'''

while_number = 0 # Start with 0
while_sum = 0 # Start with a sum of 0

while while_sum < 10:
    print('%i + %i = %i'%(while_sum, while_number, while_sum + while_number))
    
    while_sum = while_sum + while_number # Add the number to the sum
    while_number = while_number + 1 # Increase the number by 1

# This next line won't execute until the loop is done
print("The sum is %i, and the last number is %i"%(while_sum,while_number))

###############################################################################

# Task) Construct a while loop which starts with the number 100 
#       and keeps subtracting 7 until the number is less than 30
#
#       Write your code below



###############################################################################

'''
A for loop is constructed like this:

for i in your_list:
    # what to do for each i in the list
    
Unlike a while loop, this will not go on forever.
It will only evaluate as many times as the length of your_list.
Notice the indentations!
'''

for_sum = 0 # Start with a sum of 0
for i in range(1,11,1):
    print('%i + %i = %i'%(for_sum, i, for_sum+i))
    for_sum += i # A faster way to write "for_sum = for_sum + i"

print('The final sum is', for_sum)

###############################################################################

# Task) Construct a for loop which adds the even numbers 
#       from 0 to 100, inclusive
#
#       Write your code below





###############################################################################

'''
A function should be defined as follows:

def function_name(your_inputs)
    # type all of the operations
    return your_outputs
    
Make sure everything inside of the function is INDENTED
'''

def sum_diff(a,b):
    c = a + b
    d = a - b
    return c, d

'''
Once you define a function, you can save the outputs it generates 
from any valid inputs:

[output_values] = function_name(input_values)

Below, we will save the sum and difference of 3 and 4.
'''

[test_sum, test_diff] = sum_diff(3,4)

print("Sum = %i, Difference = %i"%(test_sum,test_diff))

###############################################################################

# Task) Make a function which returns c, the product of inputs a and b
#
#       Write your code below




###############################################################################