#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import sqlite3

# dataset and first few cells inspired by https://www.datacamp.com/community/tutorials/scikit-learn-tutorial-baseball-1
# Connecting to SQLite Database
conn = sqlite3.connect('lahman2016.sqlite')


# In[3]:


query = '''select * from Teams 
inner join TeamsFranchises
on Teams.franchID == TeamsFranchises.franchID
where Teams.G >= 150 and TeamsFranchises.active == 'Y';
'''

# Creating dataframe from query.
Teams = conn.execute(query).fetchall()


# In[4]:


# Convert results to DataFrame
teams_df = pd.DataFrame(Teams)

# Print out first 5 rows
print(teams_df.head())


# In[5]:


# Adding column names to dataframe
cols = ['yearID','lgID','teamID','franchID','divID','Rank','G','Ghome','W','L','DivWin','WCWin','LgWin','WSWin','R','AB','H','2B','3B','HR','BB','SO','SB','CS','HBP','SF','RA','ER','ERA','CG','SHO','SV','IPouts','HA','HRA','BBA','SOA','E','DP','FP','name','park','attendance','BPF','PPF','teamIDBR','teamIDlahman45','teamIDretro','franchID','franchName','active','NAassoc']
teams_df.columns = cols

# Print the first rows of `teams_df`
print(teams_df.head())

# Print the length of `teams_df`
print(len(teams_df))


# In[6]:


# Dropping your unnecesary column variables.
drop_cols = ['lgID','franchID','divID','Rank','Ghome','L','DivWin','WCWin','LgWin','WSWin','SF','name','park','attendance','BPF','PPF','teamIDBR','teamIDlahman45','teamIDretro','franchID','franchName','active','NAassoc']

df = teams_df.drop(drop_cols, axis=1)

# Print out first rows of `df`
print(df.head())


# In[7]:


# Print out null values of all columns of `df`
print(df.isnull().sum(axis=0).tolist())


# In[8]:


# import the pyplot module from matplotlib
import matplotlib.pyplot as plt

# matplotlib plots inline  
get_ipython().run_line_magic('matplotlib', 'inline')

# Plotting distribution of wins
plt.hist(df['W'])
plt.xlabel('Wins')
plt.title('Distribution of Wins')

plt.show()


# In[ ]:




