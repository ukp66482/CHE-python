#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Auto-resolve the single-unit mass-balance problems (without reactions)

# Cleared all the stored variables from previous calculations
get_ipython().run_line_magic('reset', '-f')

import numpy as np
import pandas
import sympy
from termcolor import colored

###### inputs
stream_direction = ["in","out", "out"] # directions of streams
component_labels = ["Flow rate", "Oxygen", "Nitrogen", "Argon"]
fraction_prefix = "y" # mass (x) or mole (y) fraction
y1N = 0.7808
F2 = 100
y2O = 0.9
y1O = 0.2098
y2N = 0.02
y3A = 0
######

###### solving procedure

# Find the values for the number of streams (Ns) and components (Nc)
Ns = len(stream_direction)
Nc = len(component_labels) - 1 # -1 because flowrate is not included

# Prepare stream labels for the flow table
stream_labels = []
for i in range(Ns):
    # Append the stream labels
    stream_labels.append("stream " + str(i+1) + "-" + stream_direction[i])

# Create an empty array for the flow table
# Nc+1 becasue we have to include the flowrate in the table
# dtype=object because we have to use object-type instead of number-type
V_empty = np.empty([Ns, Nc+1],dtype=object)  

# Showing the flow table with stream and component labels
df = pandas.DataFrame(V_empty, index=stream_labels, columns=component_labels)
print (df)

# Prepare an empty list for storing all variable names
all_variables = []

# Loop the streams to generate flow rate names
for i in range(len(stream_direction)):
    all_variables.append(component_labels[0][0] + str(i+1))

# Loop the components and streams to generate fraction names
for i in range(len(component_labels[1:])):  #starting from 1 because flowrate is not included
    for j in range(len(stream_direction)):
        all_variables.append(fraction_prefix + str(j+1) 
                             + component_labels[i+1][0])
        
# Declare the symbols based on the variables
all_symbols = sympy.symbols(all_variables)

# Create a duplicate array for inserting the variables
V_initial = V_empty.copy()

given_variables = []
# Loop all the variables and insert into the new flow table (V_initial)
for i in range(len(all_variables)):
    
    # Find the row index for inserting variables, based on the stream number
    index_row = int(all_variables[i][1]) - 1
    
    # if the 1st string of the variable name equals to the "F" (or any name you defined)
    # the column index should be zero (1st column)
    if all_variables[i][0] == component_labels[0][0]:
        index_column = 0
    
    # if not flowrate, it should be components
    else:
        for j in range(len(component_labels)):
            
            #find the column index by matching the variable names and component labels
            if all_variables[i][2] == component_labels[j][0]:
                index_column = j
    
    # Check if the variable has been given values (input)
    if all_variables[i] in globals():
        # insert the value into the new array
        V_initial[index_row, index_column] = eval(all_variables[i])
        given_variables.append(all_variables[i])
    # If the variable has not been given (wait to be resolved)
    else:
        # insert a symbol into the new array
        V_initial[index_row, index_column] = all_symbols[i]

#Print an empty line
print("\n")

# Show the flow table 
df = pandas.DataFrame(V_initial, index=stream_labels, columns=component_labels)
print (df)   

# Calculate the relevent number of variables
N_zeros = np.count_nonzero(V_initial == 0) # Number of zeros
Nv = Ns*(Nc+1) - N_zeros # Total variables (zeros not included)
Nd = Nv - Ns - Nc # Design variables

# Print the information
print ("\nThe number of total variables (zeros not included):", Nv) # \n is used to add a new line
print (colored("The number of design variables:",attrs=["bold"]), Nd)
print ("(The number of inputs that you have to assign)")
print ("\nYou have given", len(given_variables)-N_zeros, "variables")

# Check if you have given too many or didn't give enough design variables
if len(given_variables)-N_zeros > Nd:
    print (colored("You have given too many input variables","red"))
if len(given_variables)-N_zeros < Nd:
    print (colored("You didn't give enough input variables","red"))

# List all the unknown (waited to be resolved) variables    
unknown_variables = [element for element in all_variables if element not in given_variables]
number_unknowns = len(unknown_variables)
print ("\nThere are", number_unknowns, "unknown variables:")
print (*unknown_variables,sep=" ,")






