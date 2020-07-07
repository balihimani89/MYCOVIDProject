#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import tkinter as tk
import pandas as pd


# In[2]:


pwd


# In[3]:


data = pd.read_csv('STATE_WISE_COVID_DATA.csv')


# In[4]:


data.head(39)


# In[5]:


window = tk.Tk()

window.geometry("600x500")

window.title("Pandemic Analytics Engine for COVID_19 2020")

window.configure(background='Light Grey')


# In[6]:


tk.Label(window,text = "Pandemic Analyzer COVID_19", bg='Light Grey' ,fg = 'Dark Blue',font = "none 14 bold").grid(row = 0,column = 0,sticky= 'W')


# In[7]:


tk.Label(window,text = "Select State of India", bg='Light Grey' ,fg = 'White',font = "none 14 bold").grid(row = 2,column = 0,sticky= 'W')


# In[8]:


variable = StringVar(window)

variable.set(data.State[0]) 

w = OptionMenu(window, variable, *data.State)
w.grid(row=2,column=6,sticky='W')


# In[9]:


global inf 
global rec 
global dec

def click():
   

    inf = tk.Label(window,text = int(data[data.State == variable.get()].Confirmed), bg='Orange' ,fg = 'Black',font = "none 14 bold").grid(row = 4,column = 6,sticky= 'W')
    rec = tk.Label(window,text = int(data[data.State == variable.get()].Recovered), bg='Orange' ,fg = 'Black',font = "none 14 bold").grid(row = 6,column = 6,sticky= 'W')
    dec = tk.Label(window,text = int(data[data.State == variable.get()].Deceased), bg='Orange' ,fg = 'Black',font = "none 14 bold").grid(row = 8,column = 6,sticky= 'W')


# In[10]:


Button(window,text = 'OK',width = 6,command = click).grid(row = 2,column=10,sticky = 'W')


# In[11]:


tk.Label(window,text = "Infected", bg='Light Grey' ,fg = 'Orange',font = "none 14 bold").grid(row = 4,column = 0,sticky= 'W')


# In[12]:


tk.Label(window,text = "Recovered", bg='Light Grey' ,fg = 'sea green',font = "none 14 bold").grid(row = 6,column = 0,sticky= 'W')


# In[13]:


tk.Label(window,text = "Deceased", bg='Light Grey' ,fg = 'red3',font = "none 14 bold").grid(row = 8,column = 0,sticky= 'W')


# In[14]:


def ifr():
    inf = tk.Label(window,text = int((inf/dec)*100), bg='Orange' ,fg = 'Black',font = "none 14 bold").grid(row = 12,column = 6,sticky= 'W')


# In[15]:


btn1 = tk.Button(window,text = 'IFR',width = 6,command = ifr).grid(row = 10,column=2,sticky = 'W')


# In[16]:


tk.Label(window,text = "Value", bg='Light Grey' ,fg = 'RoyalBlue1',font = "none 14 bold").grid(row = 12,column = 0,sticky= 'W')


# In[17]:


window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




