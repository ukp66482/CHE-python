#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import pandas
import sympy

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
                             + component_labels[i][0])
        
# Declare the symbols based on the variables
all_symbols = sympy.symbols(all_variables)

