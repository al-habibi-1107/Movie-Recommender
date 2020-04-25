#!/usr/bin/env python
# coding: utf-8

# In[29]:


#importing necessary libraries
import pandas as pd
import numpy as np


# In[30]:


#enter the path where you stored the netflix_titles.csv file
data= pd.read_csv("/Users/kamilanwar/Documents/Movie Recommender/netflix_titles.csv")
data.head()


# In[31]:


#Taking input from the user about their liked movies
usr_input=input('Tell us about your last watched Netflix which you loved: ')


# In[44]:



recent_movie=data[data['title']== usr_input]
recent_movie


# In[33]:


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


# In[34]:


#The dataframe is now sorted in terms of similar listing
recommend= data[data['listed_in']== genre ]
recommend.head()


# In[35]:


#code to get the rating of the show given by the user
rating= recent_movie['rating']
str(rating)
rating=str(rating)
i=0
while(not rating[i].isalpha()):
    i=i+1
rating=rating[i:]
i=0
while(not rating[i]== '\n'):
    i=i+1
rating=rating[0:i]
rating


# In[39]:


#The dataframe is further classified on basis of similar rating
recommend= recommend[recommend['rating']== rating ]
recommend.head()


# In[37]:


#code to get the type attribute of the movie read from the user
mv_type=recent_movie['type']
mv_type=str(mv_type)
i=0
while(not mv_type[i].isalpha()):
    i=i+1
mv_type=mv_type[i:]
i=0
while(not mv_type[i]== '\n'):
    i=i+1
mv_type=mv_type[0:i]
mv_type


# In[40]:


#the dataframe is now also considerate on the type attribute of the similar results
recommend= recommend[recommend['type']== mv_type ]
recommend.head()


# In[41]:


#the final results are displayed
print('The movies you should watch based on the last watched are:')
recommend.head()


# In[ ]:





# In[ ]:




