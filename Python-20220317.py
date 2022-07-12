#!/usr/bin/env python
# coding: utf-8

# In[69]:


# An alternative way of expressing equations

import sympy

x, y = sympy.symbols("x, y")
eq = (x - 2)**2 + (y - 3)**2 
expression_eq = sympy.Eq(eq, 8)

# Show the equation 
expression_eq


# In[70]:


# Solve the equation
solution = sympy.solve(expression_eq, x)
print (solution)


# In[71]:


# show one of the solution 
solution[0]


# In[72]:


# Enter the value for y and return the solution
solution[0].subs(y, 3)


# In[73]:


# Convert the solution to float number
float (solution[0].subs(y, 3))


# In[74]:


# Solve the complicated problems (please check the slide file for the solving process) 

import numpy as np

variable_names = ["F1", "F3", "y2N", "y2A"]

#### solving simutaneous equations by matrix

# Coefficient matrix (n x n)
A = np.array([
    [0.2098, -0.047, 0, 0], 
    [0.7808, -0.953, -100, 0],
    [0.0094, 0, 0, -100],
    [0, 0, 1, 1]
])

# Constant matrix (n x 1)
B = np.array(
    [90, 0, 0, 0.1]
)

sol = np.linalg.solve(A, B)

####


# Show the solutions with their variable names
for i in range(len(variable_names)):
    print (variable_names[i], " = ", sol[i])

