#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt

R = 0.082 # L atom K-1 mol-1
T = 373 # Kelvin

# For CH4
# data from https://www.engineeringtoolbox.com/non-ideal-gas-van-der-Waals-equation-constants-gas-law-d_1969.html
a = 2.3
b = 0.043

# Create a linear data points for specific volume
# the starting number can be any value larger than b
# But, if the volume is small, the pressure data value will be large
# you need to adjust the ploting ragne by setting plt.xlim()
V = np.linspace(b+0.03, 1, 100)

# Find the corresponding pressure data
P = R*T/(V-b) - a/(V**2)

# Find the compressibility
Z = P*V/R/T

plt.plot(P, Z)
plt.title("CH4")
plt.xlabel("Pressure (atm)")
plt.ylabel("Compressibility, Z")


# In[4]:


import numpy as np
import matplotlib.pyplot as plt

R = 0.082 # L atom K-1 mol-1
T = 373 # Kelvin

gas_name = ["N2", "CH4", "C2H6"]
A = [1.37, 2.3, 5.57]
B = [0.0387, 0.043, 0.06499]

for i in range(len(gas_name)):
    V = np.linspace(B[i] + 0.03, 1, 100)
    P = R*T/(V-B[i]) - A[i]/(V**2)
    Z = P*V/R/T
    
    plt.plot(P, Z, label=gas_name[i])

plt.legend()    
plt.xlabel("Pressure (atm)")
plt.ylabel("Compressibility, Z")


# In[ ]:




