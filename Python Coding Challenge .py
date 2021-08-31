#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python Coding challenge
#Loading Libraries
#numpy

import numpy as np


# In[2]:


#pandas

import pandas as pd


# In[3]:


#json

import json


# In[7]:


#Reading Dataset from URL
#Loading the json file as a dataframe

df = pd.read_json("https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json")


# In[8]:


print(df)


# In[10]:


#The defined variables of interest

module = df[["communities_villages", "water_functioning"]]


# In[11]:


print(module)


# In[14]:


#The number of water points that are functional

moduleA = df.groupby(['water_functioning'])['communities_villages'].count()


# In[15]:


print(moduleA)


# In[17]:


#The number of water points per community

moduleB = df.groupby(['communities_villages'])['water_functioning'].count()


# In[18]:


print(moduleB)


# In[71]:


#The rank of each community by the percentage of broken water points

moduleC = df[["communities_villages", "water_point_condition"]]


# In[72]:


counts = moduleC.value_counts()


# In[73]:


print(counts)


# In[74]:


percent = moduleC.value_counts(normalize = True)


# In[75]:


print(percent)


# In[76]:


percent100 = moduleC.value_counts(normalize = True).mul(100).round(1).astype(str) + '%'


# In[77]:


print(percent100)


# In[ ]:




