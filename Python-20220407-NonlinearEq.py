#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y1 = x**2 + x - 1
y2 = 5*x + 50 

plt.plot(x, y1, color="g")
plt.plot(x, y2, color="r", linestyle=":")
plt.show()


# In[43]:


# get the roots via sympy

import sympy

sympy.init_printing() # Output the equations or roots in a much clear way


X, Y = sympy.symbols("X, Y")
eq1 = sympy.Eq(X**2 + X - 1 - Y,0)
eq2 = sympy.Eq(5*X + 50 - Y, 0)

solution_sympy = sympy.solve([eq1,eq2],[X,Y])

for i in solution_sympy:
    print ("x = ", float(i[0]), "y = ", float(i[1]))


# In[44]:


# get the root via scipy

from scipy.optimize import fsolve

def equations(V):
    A, B = V
    return (A**2 + A - 1 - B,
           5*A + 50 - B)

solution_scipy = fsolve(equations,[10,100]) # The starting number can be tuned to find the closest root
solution_scipy

