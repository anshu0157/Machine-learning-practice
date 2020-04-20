#!/usr/bin/env python
# coding: utf-8

# # NUMPY MODULE

# In[1]:


import numpy as np


# In[16]:


#if there is mixed type elements in array then in numpy array all elements converted into highest dtype order
a=[2,3,4,'d',0,8]
b=[2,3,4,9.0,8.99]
print(repr(np.array(a)))#all converted into string
print(repr(np.array(b)))#all converted into float


# In[22]:


#copying
a=np.array([2,3,4,5,6,7])
b=a#if we change the value in b then value of a will be changed to
c=a.copy()#if we change the avalue in c value of a will not be change
b,c
b[1]=20
c[-1]=40
a #value of a[1] is changed but value of a[-1] is not changed


# In[32]:


#casting
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.astype.html
a=np.array([2,3,4,5,6,7])
arr=a.astype(np.float64)
print(repr(arr))
a.dtype


# In[34]:


#NaN
#When we don't want a NumPy array to contain a value at a particular index, we can use np.nan to act as a placeholder.
#A common usage for np.nan is as a filler value for incomplete data.
arr=np.array([np.nan,56,90,0])
arr


# In[35]:


#Infinity
#To represent infinity in NumPy, we use the np.inf special value. We can also represent negative infinity with -np.inf.
arr=np.array([5,6,7,np.inf,90,56,-np.inf])
arr


# # NUMPY BASICS

# np.arange function

# In[51]:


#it is used to create of large range value and it always return 1-D array
'''If only a single number, n, is passed in as an argument, np.arange will return an array with all the integers in the range [0, n). Note: the lower end is inclusive while the upper end is exclusive.
For two arguments, m and n, np.arange will return an array with all the integers in the range [m, n).
For three arguments, m, n, and s, np.arange will return an array with the integers in the range [m, n) using a step size of s.
Like np.array, np.arange performs upcasting. It also has the dtype keyword argument to manually cast the array.'''
arr=np.arange(20)
arr1=np.arange(5,30)
arr2=np.arange(5,30,3)
print(repr(arr))
print(repr(arr1))
print(repr(arr2))


# np.linspace

# In[64]:


#https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html#numpy.linspace
'''numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)'''
#This function takes in a required first two arguments, for the start and end of the range
#if you want to exclude endpoints you need to assign endpoint=False
arr=np.linspace(20,1,num=4,endpoint=False)
arr

np.reshape() function
# In[141]:


#https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html
#numpy.reshape(a, newshape, order='C')
arr=np.arange(500,dtype=np.float64)
arr
reshape=np.reshape(arr,(-1,2,10))
print(reshape.shape)
ar=reshape.flatten()#it reshape the array in 1-D array
ar.shape

np.transpose
# In[148]:


#it transpose the matrix
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.transpose.html
'''numpy.transpose(a, axes=None)'''
a=np.transpose(reshape,axes=(2,1,0))
a.shape

np.zeros and np.ones
# In[155]:


a=np.zeros(8).reshape(-1,2,2)
print(repr(a))
b=np.ones(9)
b


# # Numpy maths

# #mathematical functions
# https://numpy.org/doc/stable/reference/routines.math.html?highlight=mathematical%20functions
# 

# In[179]:


#arithmatic operations
arr=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[7,8,9],[9,6,7]])
print(arr*2.1,
      arr2 - 2,
      arr+8,
      arr//3)

Non-linear functions
Exponential and logirathic
# In[199]:


#exponential
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.exp.html
#numpy.exp(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) = <ufunc 'exp'>
#Calculate the exponential of all elements in the input array.
#e=2.7182
#for exp2 for base 2 exponential(https://docs.scipy.org/doc/numpy/reference/generated/numpy.exp2.html)
a=np.arange(1,6)
np.exp(a)


# In[202]:


#logirathimic
# for log for base e (https://docs.scipy.org/doc/numpy/reference/generated/numpy.log.html)
#for log2 for base 2 (https://docs.scipy.org/doc/numpy/reference/generated/numpy.log2.html)
#for log10 for base 10 (https://docs.scipy.org/doc/numpy/reference/generated/numpy.log10.html)
print(np.log(a))
print(np.log2(a))
np.log10(a)


# In[208]:


#np.power
np.power(a,np.array([1,2,3,4,5]))# for power (https://docs.scipy.org/doc/numpy/reference/generated/numpy.power.html)

