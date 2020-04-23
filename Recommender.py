#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


#enter the path where you stored the netflix_titles.csv file
data= pd.read_csv("/Users/kamilanwar/Documents/Movie Recommender/netflix_titles.csv")
data.head()


# In[4]:


usr_input=input('Tell us about your last watched Netflix which you loved: ')


# In[5]:




recent_movie=data[data['title']== usr_input]
recent_movie


# In[6]:


#Converts the Genre of the movie to a string so that it can be compared later
genre= recent_movie['listed_in']     
genre=str(genre)
i=0
while(not genre[i].isalpha()):
    i=i+1
genre=genre[i:]
i=0
while(not genre[i]== '\n'):
    i=i+1
genre=genre[0:i]
genre


# In[7]:



recommend= data[data['listed_in']== genre ]
recommend.head()


# In[8]:


print('The movies you should watch based on the last watched are:')
recommend['title']


# In[ ]:





# In[ ]:




