#!/usr/bin/env python
# coding: utf-8

# # Matrix multiplication

# Since NumPy arrays are basically vectors and matrices, it makes sense that there are functions for dot products and matrix multiplication. Specifically, the main function to use is np.matmul, which takes two vector/matrix 
# arrays as input and produces a dot product or matrix multiplication.
# 
# The code below shows various examples of matrix multiplication. When both inputs are 1-D, 
# the output is the dot product.
# 
# Note that the dimensions of the two input matrices must be valid for a matrix multiplication. 
# Specifically, the second dimension of the first matrix must equal the first dimension of the 
# second matrix, otherwise np.matmul will result in a ValueError.
# 
# For matrix (https://numpy.org/doc/stable/reference/generated/numpy.matrix.html?highlight=matrix#numpy.matrix)
# 
# for matrix multiplication(https://numpy.org/doc/stable/reference/generated/numpy.matmul.html?highlight=matmul#numpy.matmul)
# 

# In[29]:


import numpy as np
arr=np.array([[9,7,6,5,7],[3,4]])
arr1=np.array([[9,8,7,7,2],[0,8,-2,9]])
arr@arr1


# In[61]:


#np.random.randint
#https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html?highlight=randint#numpy.random.randint
#numpy.random.randint(low, high=None, size=None, dtype='l')
np.random.seed(9)
print(repr(np.random.randint(4)))
print(np.random.randint(5,high=10,size=5))


# In[80]:


#np.random.shuffle(numpy array)
#https://numpy.org/doc/stable/reference/random/generated/numpy.random.shuffle.html?highlight=random%20shuffle#numpy.random.shuffle
a=np.array([[1,2,3,4],[6,7,8,9]])
print(a)
np.random.shuffle(a)
print(a)


# random distribution 
# https://numpy.org/doc/stable/reference/random/legacy.html?highlight=distributions
# look for it if you needed
# https://docs.scipy.org/doc/numpy-1.14.1/reference/routines.random.html

# In[85]:


lottery_name=['Anshu','vaibhav','nitin','rajendra']
np.random.choice(lottery_name)


# In[ ]:




