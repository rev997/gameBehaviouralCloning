#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


original=np.load('dataset.npy')


# In[3]:


final=[]


# In[4]:


for values in original:
    if values[1]>0:
        final.append([values[0],values[1]])
    if values[1]<0:
        final.append([values[0],values[1]])


# In[5]:


np.save('final_no_zeros.npy',final)

