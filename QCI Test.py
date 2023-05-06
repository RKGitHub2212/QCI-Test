#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


mh = pd.read_csv("D:\Test\Mental Health.csv")
mh


# This Dataset has 356 Rows and 10 Columns.

# In[4]:


mh.info()


# In[5]:


mh.isnull().sum()


# In this Dataset some column has null values.
# Column named floor,room and hostel has 59 Null values each.
# and column named m_health has 61 and educ_standard has 23 Null Values.

# In[6]:


mh.describe()


# From above data we can get brief information about columns in the Dataset which has numerical values.
# We can get count,mean,std,min,max,50% etc from above table.

# # Q1 - a.How many participants are there in the treatment group? And how many in the control group?

# In[7]:


mh['treatment'].value_counts()


# From above we can say that 183 particapants are in treatment group and 173 aprticipants are in Control Group.

# # b.Answer the below questions only for the ”Red hostel” in  “Karnataka” state.

# In[8]:


Karnat = mh[mh['state'] == 'Karnataka']
Karnat


# In[9]:


Red = Karnat[Karnat['hostel'] == 'Red Hostel']
Red


# # i.	How many missing values are there in the m health variable? How can you deal with the missing values?

# In[10]:


Red.isnull().sum()


# Only 1 missing value is there in column named m_health and educ_standard.
# As here we loss only 1 row so we can easily remove the row with missing values.

# # ii.	How many rooms are there in the hostel?

# In[11]:


Red.room.sum()


# There are 368 rooms in the hostel

# iii.	What is the minimum number of individuals in a room? Which room?

# # iv.	Which floor has the lowest number of rooms?

# In[13]:


rooms = Red.groupby('floor')['room'].sum()
rooms


# From above output it is clear that floor 0 has 10 rooms.

# v.	What is the average number of people per floor?

# # c.	One of the variables in this dataset records the participant’s education level.

# # i.	Generate a relationship between income and education.

# In[14]:


plt.bar(mh['educ_standard'],mh['income'])


# # ii.	In the distribution, which level of education has the lowest average income

# From above graph we can say that education level 4 has lowest average income.

# d.	Run any analysis you seem fit between mental health score and treatment indicator to study impact of the intervention. Clearly state the direction of the effect; whether the effect was significant; if yes, the level of significance.

# In[16]:


sns.heatmap(mh.corr())


# From above heatmap we can say that m_health is correlated with educ_standard , income and treatment.

# In[ ]:





# e.	Now, your research manager asks you to control for income in the regression. The income can be classified into 3 categories - low (below 30,000), middle (30,000-35,000) and high (above 35,000)

# We can create dummies variable of income and concat it with Dataset for regression as done below

# In[17]:


income_cat = pd.cut(mh['income'], bins=[0,30000,35000,float('inf')], labels=['low', 'middle', 'high'])


# In[18]:


income_dummies = pd.get_dummies(income_cat, prefix='income')


# In[19]:


pd.concat([mh, income_dummies], axis=1)


# Now we have 356 Rows and 13 Columns in Dataset.

# In[26]:


mh.to_csv('Mental Health Final.csv')


# In[27]:


mh.to_excel('Mental Health Final.xlsx')


# In[ ]:




