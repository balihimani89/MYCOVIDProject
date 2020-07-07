#!/usr/bin/env python
# coding: utf-8

# In[1]:


from  tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as mbox
from csv import reader
tkter = Tk()
tkter.geometry("350x400")
pic = PhotoImage(file="tkinter.png")
Label(tkter, image=pic,bg='snow', bd=0).pack()

# Defining Title to the application
tkter.title('IFR/CMR Caliculator')
# Reading Data from CSV file

with open('Pandamic_Analysis_THE1.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    data = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(data)
#Creating Labels 
lbl=Label(tkter, text="Select State/UT:", bg='snow',fg='black', font=("arial", 16))
lbl.place(x=0, y=30)
Confmed=Entry(bg='goldenrod')
Confmed.place(x=160, y=60,width=150,height=30)
lbl1=Label(tkter, text="Confirmed:", fg='goldenrod', font=("arial", 16))
lbl1.place(x=0, y=60)
Active=Entry(bg='green yellow')
Active.place(x=160, y=90,width=150,height=30)
lbl2=Label(tkter, text="Active:", fg='green yellow', font=("arial", 16))
lbl2.place(x=0, y=90)
Recover=Entry(bg='SlateBlue2')
Recover.place(x=160, y=120,width=150,height=30)
lbl3=Label(tkter, text="Recovered:", fg='SlateBlue2', font=("arial", 16))
lbl3.place(x=0, y=120)
Deceased=Entry(bg="red")
Deceased.place(x=160, y=150,width=150,height=30)
lbl4=Label(tkter, text="Deceased:", fg='red', font=("arial", 16))
lbl4.place(x=0, y=150)
Population=Entry()
Population.place(x=160, y=180,width=150,height=30)
lbl4=Label(tkter, text="Population:", font=("arial", 16))
lbl4.place(x=0, y=180)

data1=[]
data2=[]
#Creating List using Loop
for i in range(len(list_of_rows)):
    data1.append(list_of_rows[i])
    data2.append(data1[i][0])

#Creating Function for clearing the text boxes
def enable_items():
    Confmed.configure(state='normal')
    Active.configure(state='normal')
    Recover.configure(state='normal')
    Deceased.configure(state='normal')
    Population.configure(state='normal')
    Confmed.delete(0, 'end')
    Active.delete(0, 'end')
    Recover.delete(0, 'end')
    Deceased.delete(0, 'end')
    Population.delete(0, 'end')  
    CMRRes.configure(state='normal')
    CMRRes.delete(0, 'end')
    IFRRes.configure(state='normal')
    IFRRes.delete(0, 'end')
    
##Creating Function for population data into text boxes and disabling it
def on_state_changed():
    #print(data1)
    enable_items()
    for i in range(len(data1)):
            #print(data1)
    
            dat=data1[i][0]
            if cb.get()==dat:
                Confmed.insert(END, data1[i][1])
                Active.insert(END, data1[i][2])
                Recover.insert(END, data1[i][3])
                Deceased.insert(END, data1[i][4])
                Population.insert(END, data1[i][5])
                Confmed.configure(state='disabled')
                Active.configure(state='disabled')
                Recover.configure(state='disabled')
                Deceased.configure(state='disabled')
                Population.configure(state='disabled')
#Settingup Data for Combobox
cb=Combobox(tkter,values=data2)
cb.place(x=160, y=30,width=150,height=30)

clk = Button(tkter, text='Click',bg="snow",fg="red",command=on_state_changed)
clk.place(x=310, y=30,height=30)
#print(data1)

#Creating function for IFR caliculation
def ifr():
        num1=int(Confmed.get())
        num2=int(Active.get())
        num3=int(Recover.get())
        num4=int(Deceased.get())
        num5=int(Population.get())
        if num1==num2+num3+num4:
            result=round((num4/num1)*100,2)
            IFRRes.insert(END, str(result))
            IFRRes.configure(state='disabled')
        else:
            mbox.showinfo('Message','You entered Invaild Numbers')
            Active.delete(0, 'end')
            Recover.delete(0, 'end')
            Deceased.delete(0, 'end')
            Confmed.delete(0, 'end')

#Creating function for CMR caliculation
def cmr():
        num1=int(Confmed.get())
        num2=int(Active.get())
        num3=int(Recover.get())
        num4=int(Deceased.get())
        num5=int(Population.get())
        if num1==num2+num3+num4:
            result=round((num4/num5)*100,2)
            CMRRes.insert(END, str(result)) 
            CMRRes.configure(state='disabled')
        else:
            mbox.showinfo('Message','You entered Invaild Numbers')
            Active.delete(0, 'end')
            Recover.delete(0, 'end')
            Deceased.delete(0, 'end')
            Confmed.delete(0, 'end')
        
#creating Buttons             
IFR = Button(tkter, text='CHECK  IFR',bg="blue",fg="white",command=ifr)
IFR.place(x=150, y=230)
CMR=Button(tkter, text='CHECK  CMR',bg="green",fg="white",command=cmr)
CMR.place(x=250, y=230)
IFRRes=Entry()
IFRRes.place(x=160, y=260,width=150,height=30)
lbl5=Label(tkter, text="IFR Result:", fg='black', font=("arial", 16))
lbl5.place(x=0, y=260)
lbl5=Label(tkter, text="IFR Formula: Deceased/Confirmed", fg='red', font=("arial", 10))
lbl5.place(x=100, y=300)
CMRRes=Entry()
CMRRes.place(x=160, y=330,width=150,height=30)
lbl6=Label(tkter, text="CMR Result:", fg='black', font=("arial", 16))
lbl6.place(x=0, y=330)
lbl5=Label(tkter, text="CMR Formula: Deceased/Population", fg='red', font=("arial", 10))
lbl5.place(x=100, y=370)
tkter.mainloop()


# In[ ]:





# In[ ]:




