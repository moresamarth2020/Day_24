#!/usr/bin/env python
# coding: utf-8

# # Python Sets
# Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

# In[1]:


info = {"Carla", 19, False, 5.9, 19}
print(info)


# In[3]:


st = { }
print(type(st))


# ## Accessing set items:
# #### Using a For loop
# You can access items of set using a for loop.

# In[4]:


info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)


# In[ ]:




