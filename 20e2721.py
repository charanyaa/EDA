#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


df=pd.read_csv('d:\\australian_capital_retail.csv',encoding='latin-1')
df.head()


# In[10]:


df.describe()


# In[11]:


df.info()


# In[13]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12, 6)
sns.barplot(x="month",y="other_retailing",data=df)


# In[14]:


df.corr()


# In[15]:


sns.heatmap(df.corr())


# In[20]:


month_name=df.month.value_counts().index
other_retailing_val=df.other_retailing.value_counts().values


# In[21]:


plt.pie(other_retailing_val[:3],labels=month_name[:3],autopct='%1.2f%%')


# In[22]:


df


# In[23]:


df.columns


# sns.countplot(x="month",data=df,palette=['white','red','orange','yellow','black','pink'])

# In[30]:


df.groupby(['month','other_retailing']).size().reset_index().head(5)


# In[ ]:




