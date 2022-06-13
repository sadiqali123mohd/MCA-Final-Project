from time import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.tix import LabelEntry
from colorama import Cursor
import mysql.connector
import csv
import os
mydata=[]
# text variable


def update(rows):
    global mydata
    mydata=rows
    tree.delete(*tree.get_children())
    for i in rows:
        tree.insert('','end',values=i)


def search():
    q2=sid.get()
    query="select * from attendance where course LIKE '%"+q2+"%'  OR Student_name LIKE '%"+q2+"%' or date LIKE '%"+q2+"%'"
    my_cursor.execute(query)
    rows=my_cursor.fetchall()
    update(rows)

def punctual():
    query="select  DISTINCT * from attendance where time between '08:30:00' and '08:45:00'"
    my_cursor.execute(query)
    rows=my_cursor.fetchall()
    update(rows)

def defaulter():
    query="select DISTINCT  * from attendance where  not time between '08:30:00' and '08:45:00'"
    my_cursor.execute(query)
    rows=my_cursor.fetchall()
    update(rows)
def random():
    query="select * from attendance where time between '08:30:00' and '08:45:00' order by RAND() LIMIT 1"
    my_cursor.execute(query)
    rows=my_cursor.fetchall()
    update(rows)


# Clear function
def clear():
    query="select * from attendance"
    my_cursor.execute(query)
    rows=my_cursor.fetchall()
    update(rows)

def getrow():
    return True

def export():
    if len(mydata)<1:
        messagebox.showerror("error","no data is available to export ")
        return False
    fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="save csv",filetypes=(("CSV File","*.csv"),("All Files","*.*")))
    with open(fln,mode='w') as myfile:
        exp_writer=csv.writer(myfile,delimiter=',')
        for i in mydata:
            exp_writer.writerow(i)
    messagebox.showinfo("data exported","your data are exported "+os.path.basename(fln)+"  succesfully")
def mport():
    mydata.clear()
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="OPEN CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")))
    with open(fln) as myfile:
        csvread=csv.reader(myfile,delimiter=',')
        for i in csvread:
            mydata.append(i)
    update(mydata)
def save():
    if messagebox.askyesno("confiramtion","are u sure want to save the data"):
        print(mydata)
        for i in mydata:
            Student_id=i[0]
            Student_name=i[1]
            Course=i[2]
            Branch=i[3]
            Time=i[4]
            Date=i[5]                        
            query="INSERT INTO attendance(Student_id,Student_name,Course,Branch,Time,Date) values(%s,%s,%s,%s,%s,%s)"
            my_cursor.execute(query,(Student_id,Student_name,Course,Branch,Time,Date))
        conn.commit()
        
        messagebox.showinfo("data save","data save succesfully")
    else:
        return False

        

conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
my_cursor=conn.cursor()

root=Tk()
sid=StringVar()
wrapper1=LabelFrame(root,text="Report")
wrapper1.pack(fill="both",expand="yes",padx=20,pady=10)
wrapper2=LabelFrame(root,text="Search")
wrapper2.pack(fill="both",expand="yes",padx=20,pady=10)

tree=ttk.Treeview(wrapper1,column=(1,2,3,4,5,6),show="headings",height="6")
tree.pack()
tree.heading(1,text="Student_Id")
tree.heading(2,text="Student Name")
tree.heading(3,text="Course")
tree.heading(4,text="Branch")
tree.heading(5,text="Time")
tree.heading(6,text="Date")
tree.bind('<Double 1>',getrow)

export1=Button(wrapper1,text="Export csv",command=export,width=15,activebackground = "Red",font=("times new roman",12,"bold"),bg="blue")
export1.pack(side=tk.LEFT,padx=10,pady=10)
importb=Button(wrapper1,text="import",command=mport,width=15,activebackground = "Red",font=("times new roman",12,"bold"),bg="blue")
importb.pack(side=tk.LEFT,padx=10,pady=10)

isavedata=Button(wrapper1,text="savedata",command=save,width=15,activebackground = "Red",font=("times new roman",12,"bold"),bg="blue")
isavedata.pack(side=tk.LEFT,padx=10,pady=10)

iexit=Button(wrapper1,text="Exit",width=15,activebackground = "Red",font=("times new roman",12,"bold"),bg="blue",command=lambda:exit())
iexit.pack(side=tk.LEFT,padx=10,pady=10)

query="select * from attendance"
my_cursor.execute(query)
rows=my_cursor.fetchall()
update(rows)


# search 
lbl=Label(wrapper2,text="search",width=15,activebackground = "Red",font=("times new roman",12,"bold"),bg="light blue")
lbl.pack(side=tk.LEFT,padx=10)
searchentry=Entry(wrapper2,textvariable=sid,width=15)
searchentry.pack(side=tk.LEFT,padx=15,pady=18)
btn=Button(wrapper2,text="search",command=search,width=15,activebackground = "Red",font=("times new roman",12,"bold"),bg="blue")
btn.pack(side=tk.LEFT,padx=6)



# clear button
clear=Button(wrapper2,text="Show All",command=clear,width=15,activebackground = "Red",font=("times new roman",12,"bold"),bg="blue")
clear.pack(side=tk.LEFT,padx=6)

btn1=Button(wrapper2,text="Punctual",command=punctual,width=15,activebackground = "Red",font=("times new roman",12,"bold"),bg="green")
btn1.pack(side=tk.LEFT,padx=6)
btn2=Button(wrapper2,text="Defaulter",command=defaulter,width=15,activebackground = "Red",font=("times new roman",12,"bold"),bg="green")
btn2.pack(side=tk.LEFT,padx=6)
btn3=Button(wrapper2,text="random winner",command=random,width=15,activebackground = "Red",font=("times new roman",12,"bold"),bg="green")
btn3.pack(side=tk.LEFT,padx=18)













root.title("report")
root.geometry("1600x770")
root.mainloop()