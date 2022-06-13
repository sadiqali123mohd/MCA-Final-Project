from tkinter  import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from student import Student
import os
from report import Report
from facerecog import Face_recognition
from train import Train 
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1650x770+0+0")
		# self.root.geometry("1530x770+0+0")
        self.root.title("Punctuality Drive")
#first image
        img=Image.open("college images//student.jpeg")
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
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
