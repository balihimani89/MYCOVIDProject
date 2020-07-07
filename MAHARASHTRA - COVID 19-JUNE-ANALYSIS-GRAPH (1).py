#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv('MAHARASHTRA_DATA_JUNE.csv')


# In[3]:


data.head(30)


# In[4]:


data.plot(y=['Cured','Deaths','Confirmed'], x='Date')


# In[5]:


data.plot.bar(y=['Cured','Deaths','Confirmed'], x='Date')


# In[6]:


plt.plot(data['Date'],data['Cured'],'g',label='Cured', linewidth=5)
plt.plot(data['Date'],data['Deaths'],'c',label='Deaths', linewidth=5)
plt.plot(data['Date'],data['Confirmed'],'b',label='Confirmed', linewidth=5)
plt.title('MAHARASHTRA - COVID 19-JUNE-ANALYSIS')
plt.ylabel('Number of Persons')
plt.xlabel('Day of June 2020')
plt.legend()
plt.grid(True,color='k')
plt.savefig('PAMLPlot1.png')
plt.show()


# In[7]:


plt.plot(data['Date'],data['Cured'],'g',label='Cured', linewidth=5)
plt.plot(data['Date'],data['Deaths'],'c',label='Deaths', linewidth=5)
plt.plot(data['Date'],data['Confirmed'],'b',label='Confirmed', linewidth=5)
plt.title('MAHARASHTRA - COVID 19-JUNE-ANALYSIS')
plt.ylabel('Number of Persons')
plt.xlabel('Day of June 2020')
plt.legend()
plt.grid(True,color='k')
plt.savefig('MAHARASHTRA - COVID 19-JUNE-ANALYSIS.png')
plt.show()


# In[8]:


IFR_MAHARASHTRA=(data['Cured']/data['Deaths'])*100


# In[9]:


IFR_MAHARASHTRA


# In[10]:


plt.plot(data['Date'],IFR_MAHARASHTRA,'g',label='MAHARASHTRA', linewidth=5)
plt.title('MAHARASHTRA - COVID 19-JUNE-ANALYSIS_IFR')
plt.ylabel('IFR=No. of Recovered/ No. of Death due to Corona')
plt.xlabel('Day of June 2020')
plt.legend()
plt.grid(True,color='k')
plt.savefig('MAHARASHTRA - COVID 19-JUNE-ANALYSIS-IFR.png')
plt.show()


# In[11]:


data_TELANGANA = pd.read_csv('TELANGANA_DATA_JUNE.csv')


# In[12]:


IFR_TELANGANA=(data_TELANGANA['Cured']/data_TELANGANA['Deaths'])*100


# In[13]:


IFR_TELANGANA


# In[14]:


plt.plot(data_TELANGANA['Date'],IFR_TELANGANA,'g',label='IFR_TELANGANA', linewidth=5)
plt.plot(data['Date'],IFR_MAHARASHTRA,'c',label='IFR_MAHARASHTRA', linewidth=5)
plt.title('TELANGANA-MAHARASHTRA- COVID 19-JUNE-ANALYSIS-IFR')
plt.ylabel('IFR=No. of Recovered/ No. of Death due to Corona')
plt.xlabel('Day of June 2020')
plt.legend()
plt.grid(True,color='k')
plt.savefig('TELANGANA-MAHARASHTRA - COVID 19-JUNE-ANALYSIS-IFR.png')
plt.show()


# In[15]:


plt.plot(data['Date'],data['Cured'],'g',label='Cured_MAHARASHTRA', linewidth=3)
plt.plot(data['Date'],data['Deaths'],'r',label='Deaths_MAHARASHTRA', linewidth=3)
plt.plot(data['Date'],data['Confirmed'],'b',label='Confirmed_MAHARASHTRA', linewidth=3)
plt.plot(data_TELANGANA['Date'],data_TELANGANA['Cured'],'c',label='Cured_TELANGANA', linewidth=3)
plt.plot(data_TELANGANA['Date'],data_TELANGANA['Deaths'],'k',label='Deaths_TELANGANA', linewidth=3)
plt.plot(data_TELANGANA['Date'],data_TELANGANA['Confirmed'],'m',label='Confirmed_TELANGANA', linewidth=3)
plt.title('TELANGANA-MAHARASHTRA- COVID 19-JUNE-ANALYSIS')
plt.ylabel('IFR=No. of Recovered/ No. of Death due to Corona')
plt.xlabel('Day of June 2020')
plt.legend()
plt.grid(True,color='k')
plt.savefig('TELANGANA-MAHARASHTRA - COVID 19-JUNE-ANALYSIS.png')
plt.show()


# In[ ]:




