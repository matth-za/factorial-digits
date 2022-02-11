#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[20]:


n = np.math.factorial(1000)

x = []
while (n > 0):
        x.append(n % 10)
        n //= 10
        
s = np.sum(x)
print(s)


# In[ ]:




