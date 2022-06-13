from tkinter  import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os 
import numpy as np
import csv
from tkinter import filedialog

class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Register")

        # variable
        self.fname=StringVar()
        self.lname=StringVar()
        self.contact=StringVar()
        self.Email=StringVar()
        self.Securityques=StringVar()
        self.securityAnswer=StringVar()
        self.Password=StringVar()
        self.Confirm_password=StringVar()


        self.bg=ImageTk.PhotoImage(file=r"D:\face recognition - Copy\college images\login.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        # left image
        self.bg1=ImageTk.PhotoImage (file=r"D:\face recognition - Copy\college images\detect.png")
        lbl_bg1=Label(self.root,image=self.bg1)
        lbl_bg1.place(x=45,y=100,width=400,height=500)



        #frame register 

        main_frame=Frame(self.root,bd=2,bg="White")
        main_frame.place(x=520,y=100,width=800,height=550)


        # label register
        register=Label(main_frame,text="Registration form",font=("times new roman",15,"bold"),fg="red",bg="white")
        register.place(x=0,y=0)

        #label entry
        firstname=Label(main_frame,text="First Name",font=("times new roman",15,"bold"),fg="red",bg="white")
        firstname.place(x=50,y=100)

        # first name entry filed
        self.fname=ttk.Entry(main_frame,textvariable=self.fname,font=("times new roman",15,"bold"))
        self.fname.place(x=50,y=130,width=200)

        # last name label and entry field

        lastname=Label(main_frame,text="lastname",font=("times new roman",15,"bold"),fg="red",bg="white")
        lastname.place(x=370,y=100)

        self.lname=ttk.Entry(main_frame,textvariable=self.lname,font=("times new roman",15,"bold"))
        self.lname.place(x=370,y=130,width=200)

        # contact 
        Contact=Label(main_frame,text="Contact",font=("times new roman",15,"bold"),fg="red",bg="white")
        Contact.place(x=50,y=170)

        self.contact=ttk.Entry(main_frame,textvariable=self.contact,font=("times new roman",15,"bold"))
        self.contact.place(x=50,y=200,width=200)

        # email
        Email=Label(main_frame,text="Email",font=("times new roman",15,"bold"),fg="red",bg="white")
        Email.place(x=370,y=170)

        self.Email=ttk.Entry(main_frame,textvariable=self.Email,font=("times new roman",15,"bold"))
        self.Email.place(x=370,y=200,width=200)


        # security question 
        securityq=Label(main_frame,text="Security Question",font=("times new roman",15,"bold"),fg="red",bg="white")
        securityq.place(x=50,y=240)

        security_combo=ttk.Combobox(main_frame,textvariable=self.Securityques,font=("times new roman",12,"bold"),state="readonly",width=16)
        security_combo["values"]=("select","your birth place","date of birth","your pet name")
        security_combo.current(0)
        security_combo.place(x=50,y=270,width=250)

# security answer
        securityAnswer=Label(main_frame,text="Security Answer",font=("times new roman",15,"bold"),fg="red",bg="white")
        securityAnswer.place(x=370,y=240)


        self.securityAnswer=ttk.Entry(main_frame,textvariable=self.securityAnswer,font=("times new roman",15,"bold"))
        self.securityAnswer.place(x=370,y=270,width=200)

        # password

        Password=Label(main_frame,text="Password",font=("times new roman",15,"bold"),fg="red",bg="white")
        Password.place(x=50,y=310)

        self.Password=ttk.Entry(main_frame,textvariable=self.Password,font=("times new roman",15,"bold"))
        self.Password.place(x=50,y=340,width=200)






        # confirm password
        Confirm_password=Label(main_frame,text="Confirm password",font=("times new roman",15,"bold"),fg="red",bg="white")
        Confirm_password.place(x=370,y=310)

        self.Confirm_password=ttk.Entry(main_frame,textvariable=self.Confirm_password,font=("times new roman",15,"bold"))
        self.Confirm_password.place(x=370,y=340,width=200)


        3# check button

       


        # signup

        img=Image.open(r"D:\face recognition - Copy\college images\register.jfif")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        Signup_btn=Button(main_frame,command=self.register,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        Signup_btn.place(x=40,y=420,width=160)

        # login now 
        img1=Image.open(r"D:\face recognition - Copy\college images\redlogin.jfif")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        Signup_btn=Button(main_frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        Signup_btn.place(x=320,y=420,width=160)




        # signup function 


    def register(self):
        if self.fname.get()=='':
            messagebox.showerror("error","please enter first name")
        elif self.lname.get()=='':
            messagebox.showerror("error","please enter last  name")
        elif self.contact.get()=='':
            messagebox.showerror("error","please enter contact no")
        elif self.Email.get()=='':
            messagebox.showerror("error","please enter email")
        elif self.Securityques.get()=='select':
            messagebox.showerror("error","please choose security question ")
        elif self.securityAnswer.get()=='':
            messagebox.showerror("error","please enter  security Answer ")
        elif self.Password.get()!=self.Confirm_password.get():
            messagebox.showerror("error ","confirm password muust be same")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from registration where email=%s")
            value=(self.Email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("error","user already exists,please try another email ")
            else:
                my_cursor.execute("insert into registration values (%s,%s,%s,%s,%s,%s,%s)",(
		        																					self.fname.get(),
																									self.lname.get(),
																									self.contact.get(),
																									self.Email.get(),
																									self.Securityques.get(),
																									self.securityAnswer.get(),
																									self.Confirm_password.get(),
																									
																									))
                                                                                                                                                                                                        
                conn.commit()
             
                conn.close()

                messagebox.showinfo("succes","Registration Succesfully ",parent=self.root)
    



















if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()