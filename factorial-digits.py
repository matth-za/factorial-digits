#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np

ip = int(input())

n = np.math.factorial(ip)

x = []
while (n > 0):
        x.append(n % 10)
        n //= 10
        
s = np.sum(x)
print(s)


# In[ ]:




