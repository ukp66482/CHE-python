#!/usr/bin/env python
# coding: utf-8

# In[8]:

### solve simple equations

import sympy 
x = sympy.symbols("X")
equation = 3*x + 4 - 17  # eq: 3x+4 = 17
solution = sympy.solve(equation)

#print the output as a fraction
print (solution[0])

#print the output as a float
print (float(solution[0]))


# In[16]:


### A different way of importing package 

from sympy import symbols
x = symbols("X")
solution = sympy.solve(3*x + 4 - 17)
##print (solution)


# In[12]:


### solve the equations of higher orders

from sympy import solve
x = sympy.symbols("X")
square_eq = x**3 -5*x + 6
sol = solve(square_eq)

print (sol)


# In[37]:


### solve simutaneous equations as matrix
# 2x + 3y = 9
# 3x + 8y = 15
# symbolize it as AM = B, M is the 

import numpy as np

A = np.array([
    [2,3], [3,8]
])

B = np.array(
    [9,15]
)

sol = np.linalg.solve(A, B)
print (sol[1])





