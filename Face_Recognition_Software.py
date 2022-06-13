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
from student import Student
import os
from report import Report
from facerecog import Face_recognition
from train import Train 

from register import Register
def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1550x800+0+0")
        self.root.title("login")
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\sadiq\Desktop\face recognition software\college images\login.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1) 



        main_frame=Frame(self.root,bd=2,bg="black")
        main_frame.place(x=610,y=170,width=340,height=450)
        title_lbl=Label(self.root,text="PUNCTUALITY DRIVE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img1=Image.open(r"C:\Users\sadiq\Desktop\face recognition software\college images\detect.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.pohotimage1=ImageTk.PhotoImage(img1)
        img1_lbl=Label(image=self.pohotimage1,bg="black",borderwidth=0)
        img1_lbl.place(x=730,y=175,width=100,height=100)
        get_str=Label(main_frame,text="Login",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #  user name label
        email=Label(main_frame,text="Email",font=("times new roman",15,"bold"),fg="white",bg="black")
        email.place(x=65,y=155)
# entry field user name
        self.txtuser=ttk.Entry(main_frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=185,width=270)
        #password
        password=Label(main_frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=65,y=225)

        # password entry
        self.txtpass=ttk.Entry(main_frame,show="*",font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)


        #### icon image
        
        img2=Image.open(r"C:\Users\sadiq\Desktop\face recognition software\college images\userlogin.jpg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.pohotimage2=ImageTk.PhotoImage(img2)
        img1_lbl=Label(image=self.pohotimage2,bg="black",borderwidth=0)
        img1_lbl.place(x=650,y=330,width=25,height=25)


## second icon
        img3=Image.open(r"C:\Users\sadiq\Desktop\face recognition software\college images\password.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.pohotimage3=ImageTk.PhotoImage(img3)
        img1_lbl=Label(image=self.pohotimage2,bg="black",borderwidth=0)
        img1_lbl.place(x=650,y=400,width=25,height=25)



        # button frame
        login_btn=Button(main_frame,text="login",command=self.login,width=15,activebackground = "green",font=("times new roman",12,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
        login_btn.place(x=110,y=300,width=120,height=35)
        
# register button
        register=Button(main_frame,text="New User Register",command=self.registerwindow,width=15,activebackground = "black",font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black")
        register.place(x=25,y=350,width=160)
# forgot password 
        forgotpassword=Button(main_frame,text="Forgot password",command=self.forgotpassword,width=15,activebackground = "black",font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black")
        forgotpassword.place(x=15,y=380,width=160)

    # register window
    def registerwindow(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

        # login function

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("error","please enter user name and password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from registration where Email=%s and Password=%s",(
                                                                    self.txtuser.get(),
                                                                    self.txtpass.get()
                                                                            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("error","invalid username and password")
            else:
                open_main=messagebox.askyesno("yes no","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            ### reset  password
    # def resetpass(self):
    #     if self.=='select':
    #         messagebox.showerror("error","please select security question",parent=self.root2)
        
    #     elif self.securityAnswer.get()=='':
    #         messagebox.showerror("error","please enter security answer",parent=self.root2)
    #     elif self.new_Password.get()=='':
    #         messagebox.showerror("error","please enter password")
    #     else:
    #         conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
    #         my_cursor=conn.cursor()
    #         query=("select * from registration where Email=%s and  Security_ques=%s and Security_Answer=%s")
    #         value=(self.txtuser.get(),self.security_combo.get(),self.securityAnswer)
    #         my_cursor.execute(query,value)
    #         row=my_cursor.fetchone()
    #         if row==None:
    #             messagebox.showerror("error","please enter correct answer",parent=self.root2)
    #         else:
    #             query=("update registration set Password=%s where Email=%s")
    #             value=(self.new_Password.get(),self.txtuser.get())
    #             my_cursor.execute(query,value)
    #             conn.commit()
    #             conn.close()
    #             messagebox.showinfo("success","your password asre succesfully reset ",parent=self.root2)





## forgot password window
    def forgotpassword(self):
        if self.txtuser.get()=='':
            messagebox.showerror("error","please enter the email adress to reset pasword")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from registration where Email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("error","please enter correct email ")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("forget password")
                self.root2.geometry("340x450+610+170")


                # label 
                forget=Label(self.root2,text="Forgot Password",font=("times new roman",15,"bold"),fg="red",bg="white")
                forget.place(x=0,y=10,relwidth=1)

                securityq=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),fg="red",bg="white")
                securityq.place(x=50,y=80)

                combobox=ttk.Combobox(self.root2,font=("times new roman",12,"bold"),state="readonly",width=16)
                combobox["values"]=("select","your birth place","date of birth","your pet name")
                combobox.current(0)
                combobox.place(x=50,y=110,width=250)
                # securityques=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),fg="red",bg="white")
                # securityques.place(x=50,y=80)

                # security_combo=ttk.Combobox(self.root2,font=("times new roman",12,"bold"),state="readonly",width=16)
                # security_combo["values"]=("select","your birth place","date of birth","your pet name")
                # security_combo.current(0)
                # security_combo.place(x=50,y=110,width=250)

        # security answer

                securityAnswer=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="red",bg="white")
                securityAnswer.place(x=50,y=150)


                self.securityAnswer=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.securityAnswer.place(x=50,y=180,width=200)
                # securityAnswer=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="red",bg="white")
                # securityAnswer.place(x=50,y=150)


                # self.securityAnswer=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                # self.securityAnswer.place(x=50,y=180,width=200)

                # password

                new_Password=Label(self.root2,text=" New Password",font=("times new roman",15,"bold"),fg="red",bg="white")
                new_Password.place(x=50,y=220)

                self.new_Password=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.new_Password.place(x=50,y=250,width=200)

                # reset 
                reset_btn=Button(self.root2,text="Reset Password",command=self.resetpass,cursor="hand2",font=("times new roman",12,"bold"),fg="white",bg="green")

                reset_btn.place(x=60,y=320,width=160)




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


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\sadiq\Desktop\face recognition software\college images\login.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        # left image
        self.bg1=ImageTk.PhotoImage (file=r"C:\Users\sadiq\Desktop\face recognition software\college images\detect.png")
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

        combobox=ttk.Combobox(main_frame,textvariable=self.Securityques,font=("times new roman",12,"bold"),state="readonly",width=16)
        combobox["values"]=("select","your birth place","date of birth","your pet name")
        combobox.current(0)
        combobox.place(x=50,y=270,width=250)

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

        img=Image.open(r"C:\Users\sadiq\Desktop\face recognition software\college images\register.jfif")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        Signup_btn=Button(main_frame,command=self.register,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        Signup_btn.place(x=40,y=420,width=160)

        # login now 
        img1=Image.open(r"C:\Users\sadiq\Desktop\face recognition software\college images\redlogin.jfif")
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
    
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1650x770+0+0")
		# self.root.geometry("1530x770+0+0")
        self.root.title("Punctuality Drive")
#first image
        img=Image.open( "college images/student.jpeg")
        img=img.resize((500,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=150)
#second image
        img1=Image.open( "college images//detect.png")
        img1=img1.resize((500,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=150)
#third image
        img2=Image.open( "college images//detect.jpg")
        img2=img2.resize((500,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=150)
        #background image
       
        img3=Image.open( "college images//bg.jpg")
        img3=img3.resize((1400,770),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1350,height=700)

        title_lbl=Label(bg_img,text="PUNCTUALITY DRIVE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        

        
# student button
        img4=Image.open( "college images//student.jpeg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=65,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


        #Detect face button
        img5=Image.open( "college images//facerecog.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=65,width=220,height=220)

        b1_1=Button(bg_img,text="face detector",cursor="hand2",command=self.face_data,font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
       
        # #Attendance 
        # img6=Image.open( "college images//detect.jpg")
        # img6=img6.resize((220,220),Image.ANTIALIAS)
        # self.photoimg6=ImageTk.PhotoImage(img6)

        # b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        # b1.place(x=800,y=65,width=220,height=220)

        # b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        # b1_1.place(x=800,y=300,width=220,height=40)
        # command=self.attendance


       
       
        # command=self.attendance
    #    ? helpdesk


        # img7=Image.open( "college images//detect.jpg")
        # img7=img7.resize((220,220),Image.ANTIALIAS)
        # self.photoimg7=ImageTk.PhotoImage(img7)

        # b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        # b1.place(x=1100,y=65,width=220,height=220)

        # b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        # b1_1.place(x=1100,y=300,width=220,height=40)
 
 
#train face data

        img8=Image.open( "college images//traindata.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=800,y=65,width=220,height=220)
        b1_1=Button(bg_img,text="Train  data",cursor="hand2",command=self.train_data,font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)
        # photos
        img9=Image.open( "college images//studentphoto.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="photos",cursor="hand2",command=self.open_img,font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=550,width=220,height=40)

#report
        img10=Image.open( "college images//report.png")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.report_gen)
        b1.place(x=210,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Report",cursor="hand2",command=self.report_gen,font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=210,y=550,width=220,height=40)
      
      
        #Exit
        img11=Image.open( "college images//exit.png")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=790,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="exit",cursor="hand2",command=self.iExit,font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=790,y=550,width=220,height=40)


    def open_img(self):
        os.startfile("data")


    #     # function button
                
    def  student_details(self):  

        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def  train_data(self):  

        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def  face_data(self):  
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
    def  report_gen(self):  
        self.new_window=Toplevel(self.root)
        self.app=Report(self.new_window)
    def  exit(self):  

        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_System(self.new_window)
    def iExit(self):
        self.iExit=messagebox.askyesno("face reecognition","are you sure want to exit this project")
        if self.iExit>0:
            self.root.destroy()
        else:
            return 
    # def  attendance(self):  

    #     self.new_window=Toplevel(self.root)
    #     self.app=Attendance(self.new_window)
    
    # def  help(self):  

    #     self.new_window=Toplevel(self.root)
    #     self.app=Helpdesk(self.new_window)














if __name__=="__main__":
    main()