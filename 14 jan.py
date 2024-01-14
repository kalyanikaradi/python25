#!/usr/bin/env python
# coding: utf-8

# # pandas

# In[ ]:


Pandas is a popular open-source data manipulation and analysis library for Python.# It provides data structures like Series and DataFrame, which are designed to handle and manipulate structured data efficiently.


# In[1]:


import pandas as pd


# In[2]:


#SERIES (Series is a one-dimensional labeled array capable of holding any data type.)
d= pd.Series()


# In[3]:


d


# In[4]:


print(type(d))


# In[5]:


#series with one element
t = (11,12,13)
d=pd.Series(t)


# In[7]:


d


# In[8]:


d=pd.Series([45,32,77,65,11,21])
d


# In[9]:


#creating series with array
#combination of numpy and pandas
import pandas as np


# In[10]:


arr=np.array([2,3,4,5])
d1=pd.Series(arr)
d1


# In[11]:


arr2=np.array([[2,3,4],[5,6,7],[8,9,10]])
arr2


# In[12]:


arr2=np.array([[1,2],[3,4],[5,6]])
arr2.shape


# In[13]:


s2=pd.Series(arr2)
s2


# In[14]:


#dict
d1={'a':1,'b':2,'c':3,'d':4}
d1


# In[15]:


d1.values()


# In[16]:


d1.items()


# In[17]:


d1.keys()


# In[18]:


d1['a']


# In[19]:


b=pd.Series(d)


# In[20]:


b


# In[21]:


b[0]


# In[22]:


b[5]


# In[ ]:




