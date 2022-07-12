#!/usr/bin/env python
# coding: utf-8

# In[59]:


### solve the linear/nonlinear simutaneous equations 

from scipy.optimize import fsolve

# variable names for printing results
variables = ["F1", "F3", "y2A", "y2N"]

def equations(V):

    F1, F3, y2A, y2N = V # Note: this implies that F1 = V[0], F3 = V[1], etc. 
    
    return (F1*0.2098 - F3*0.047 - 100*0.9,
           F1*0.7808 - F3*0.953 - 100*y2N,
           F1*0.0094 - 100*y2A,
           y2A + y2N + 0.9 - 1)
    
solutions = fsolve(equations, [200,200,0.01,0.01] )

for i in variables:
    print ("solved", i, "= ", solutions[variables.index(i)])


# In[60]:


# Solve the linear/nonlinear simutaneous equations (all equations)

# variable names for printing results
from scipy.optimize import fsolve

variables = ["F1", "F3", "y2A", "y2N", "y1A", "y3O"]

def equations(V):
    F1, F3, y2A, y2N, y1A, y3O = V
    
    return (F1*0.2098 - F3*y3O - 100*0.9, # componet O
           F1*0.7808 - F3*0.953 - 100*y2N, # component N
           F1*y1A - 100*y2A, # component A
           0.2098 + 0.7808 + y1A - 1, # stream 1
           0.9 + y2N + y2A - 1, # stream 2
           y3O + 0.953 - 1 )    # stream 3

solutions = fsolve(equations, [200,200,0.01,0.01, 0.001, 0.01 ] )

for i in variables:
    print ("solved", i, "= ", solutions[variables.index(i)])


# In[55]:


# Another way of defining equations and put them into def equations

from scipy.optimize import fsolve

# Input the functions as the string type in a list
function = ["x[0]**2 -x[1]**2 - 7", "x[0] - 2*x[1] - 2"]

def equations(x):
    
    # create a temporary list for storing eval(functions)
    temp_list = []
    
    # add each function to the temporary list after eval() operation
    for i in function:
        temp_list.append(eval(i))
    
    return (temp_list)

solutions = fsolve(equations, [0,0] )


# In[66]:


# Usage of eval function (change string to variable/equation type)

x = 5
eq = "x + 2"
eval(eq)

print ("If it doesn't use the eval function: eq =", eq)
print ("If using the eval function: eq =", eval(eq))


# In[ ]:




