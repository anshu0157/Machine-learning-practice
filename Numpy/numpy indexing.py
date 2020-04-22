#!/usr/bin/env python
# coding: utf-8

# # Indexing

# Array accessing

# In[2]:


import numpy as np


# In[151]:


#for one dimensional array
arr=np.array([1,2,3,4,5,7])
print(repr(arr[0]))
print(repr(arr[:]))
print(repr(arr[::-1]))
print(repr(arr[0:6:2]))
print(repr(arr[:-1]))
print(repr(arr[-1:]))
print(repr(arr[::2]))
np.mean(arr,axis=0)


# In[88]:


#for 2-D array
#comma is used to seperate or slice 2D array
arr1=np.arange(20).reshape(4,5)
print(repr(arr1))
print(repr(arr1[:2:]))#slice by row
print(repr(arr1[:,2:]))#slice by column
print(repr(arr1[1,2:]))
print(repr(arr1[:,:2]))
print(repr(arr1[:,2:4]))
print(repr(arr1[:1,2]))
#argmin and argmax function
print(np.min(arr1))
print(np.argmax(arr1))
print(np.argmax(arr1[:3,2]))


# In[94]:


print(np.isnan(arr1))
print(repr(np.any(arr1>3)))
print(np.all(arr1>3))


# # statistics

# https://numpy.org/doc/stable/reference/routines.statistics.html?highlight=statistic

# In[112]:


np.max(arr1),np.min(arr1),np.mean(arr1),np.var(arr1),np.median(arr1),np.sum(arr1)


# In[108]:


def ret(a):
        return np.mean(a)==np.median(a)
print(ret(arr1))
    


# In[127]:


print(arr1)
print(repr(np.max(arr1,axis=1)))
print(repr(np.mean(arr1,axis=0)))
print(repr(np.sum(arr1,axis=-1)))


# In[132]:


np.argmin(arr1),np.argmax(arr1)


# In[147]:


arr2=np.arange(20,40).reshape(4,5)
print(arr2)
print(arr1)
np.concatenate([arr1,arr2],axis=-1)


# Saving and Loading data

# In[161]:


np.save('ansh.npy',[arr1,arr2])


# In[162]:


print(repr(np.load('ansh.npy')))


# In[ ]:




