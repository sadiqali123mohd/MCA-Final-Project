from tkinter  import* 
from tkinter import ttk
from tkinter import scrolledtext
from PIL import Image,ImageTk
import tkcalendar
from tkcalendar import DateEntry

# from main import Face_Recognition_System 
 
from tkinter import messagebox
import mysql.connector 
import cv2
import os 

# from student import Student 
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x750+0+0")
        self.root.title("face recognition system")


        # varaibles
        self.var_course=StringVar()
        self.var_branch=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_sname=StringVar()
        self.var_fname=StringVar()
        self.var_dob=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_adress=StringVar()
        self.var_sid=StringVar()
        # self.var_photo=StringVar()


        #first image
        img=Image.open("college images//detect.jpg")
        img=img.resize((500,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=150)
        #second image
        img1=Image.open("college images//detect.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=150)
#third image
        img2=Image.open("college images//detect.jpg")
        img2=img2.resize((500,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=150)
#bg image
        img3=Image.open("college images//detect.jpg")
        img3=img3.resize((1400,770),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1350,height=700)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)


### home
        # home_btn=Button(bg_img,text="Home",command=self.home,width=12,font=("times new roman",12,"bold"),bg="green")
        # home_btn.grid(row=0,column=3,padx=4)

#frame creating
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1530,height=650)
#left side label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=580)
#image
        img_left=Image.open("college images//detect.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        # current course
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="current  course info",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=140)

     # course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=0,padx=2,pady=10)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","MCA","BTECH","MBA","MTECH")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #branch
        branch_label=Label(current_course_frame,text="Branch",font=("times new roman",12,"bold"),bg="white")
        branch_label.grid(row=0,column=2,padx=2,pady=10)

        branch_combo=ttk.Combobox(current_course_frame,textvariable=self.var_branch,font=("times new roman",12,"bold"),state="readonly")
        branch_combo["values"]=("Select Branch","ComputerApplication","CSE","IT","CS/ML","CS/AI","CIVIL","ME","BIO TECH")
        branch_combo.current(0)
        branch_combo.grid(row=0,column=3,padx=2,pady=10)
#year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020","2021","2022")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=2,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

         #  class student info
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Info",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=240,width=720,height=270)

        #student id
        id_label=Label(class_student_frame,text="Id:-",font=("times new roman",12,"bold"),bg="white")
        id_label.grid(row=0,column=0,padx=10,sticky=W)

        id_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        id_entry.grid(row=0,column=1,padx=10,sticky=W)
        #student name
        student_name_label=Label(class_student_frame,text="Student Name:-",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=2,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_sname,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,sticky=W)
        # bind and validation
        # validate_student_name=self.root.register(self.checkname)
        # student_name_entry.config(validate='key',validatecommand=(validate_student_name,'%P'))


        #father name
        father_name_label=Label(class_student_frame,text="Father name",font=("times new roman",12,"bold"),bg="white")
        father_name_label.grid(row=1,column=0,padx=2,sticky=W)

        father_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_fname,width=20,font=("times new roman",12,"bold"))
        father_name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # student id
        student_id_label=Label(class_student_frame,text="Student_id:-",font=("times new roman",12,"bold"),bg="white")
        student_id_label.grid(row=1,column=2,padx=2,sticky=W)

        student_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_sid,width=20,font=("times new roman",12,"bold"))
        student_id_entry.grid(row=1,column=3,padx=10,sticky=W)
        #gender 
        Gender_label=Label(class_student_frame,text="Gender:-",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=2,sticky=W)

        # Gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        # Gender_entry.grid(row=2,column=1,padx=10,sticky=W)



        Gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=16)
        Gender_combo["values"]=("select gender","Male","Female","Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)
        #Email
        Email_label=Label(class_student_frame,text="Email:-",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=4,column=0,padx=2,sticky=W)

        Email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        Email_entry.grid(row=4,column=1,padx=10,sticky=W)
        #phone 
        phoneno_label=Label(class_student_frame,text="Phone No:-",font=("times new roman",12,"bold"),bg="white")
        phoneno_label.grid(row=3,column=0,padx=2,sticky=W)

        phoneno_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phoneno_entry.grid(row=3,column=1,padx=10,sticky=W)

        # validate 
        validate_phoneno=self.root.register(self.checkcontact)
        phoneno_entry.config(validate='key',validatecommand=(validate_phoneno,'%P'))
        #adress
        Adress_label=Label(class_student_frame,text="Adress:-",font=("times new roman",12,"bold"),bg="white")
        Adress_label.grid(row=3,column=2,padx=2,sticky=W)

        Adress_entry=ttk.Entry(class_student_frame,textvariable=self.var_adress,width=20,font=("times new roman",12,"bold"))
        Adress_entry.grid(row=3,column=3,padx=10,sticky=W)
        #DOB
        DOB_label=Label(class_student_frame,text="DOB:-",font=("times new roman",12,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=2,sticky=W)
        cal=DateEntry(class_student_frame,textvariable=self.var_dob,selectmode='day',date_pattern="dd-mm-yyyy")
        # DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        cal.grid(row=2,column=3,padx=10,sticky=W)
        
        #sudent id
        student_id_label=Label(class_student_frame,text="Student_id:-",font=("times new roman",12,"bold"),bg="white")
        student_id_label.grid(row=1,column=2,padx=2,sticky=W)

        student_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_sid,width=20,font=("times new roman",12,"bold"))
        student_id_entry.grid(row=1,column=3,padx=10,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)
  
        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=160,width=650,height=35)
        #save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,activebackground = "Red",font=("times new roman",12,"bold"),bg="green")
        save_btn.grid(row=0,column=0)

        #update
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,activebackground = "Red",font=("times new roman",12,"bold"),bg="green")
        update_btn.grid(row=0,column=1)
        #delete
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,activebackground = "Red",font=("times new roman",12,"bold"),bg="green")
        delete_btn.grid(row=0,column=2)
        #reset
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,activebackground = "Red",font=("times new roman",12,"bold"),bg="green")
        reset_btn.grid(row=0,column=3)
        #button frame1
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=190,width=650,height=35)
        #take photo sample
        takephoto_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",activebackground = "Red",width=30,font=("times new roman",12,"bold"),bg="green")
        takephoto_btn.grid(row=0,column=0)
        # update photo sample 
        # takephoto_btn=Button(btn_frame1,text="Update photo sample",width=30,activebackground = "Red",font=("times new roman",12,"bold"),bg="green")
        # takephoto_btn.grid(row=0,column=1)







        #right side label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student details",font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=10,width=660,height=580)
        

        # table_frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        # table_frame.place(x=5,y=210,width=700,height=200)
        table_frame.place(x=5,y=5,width=650,height=420)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("course","branch","year","sem","id","sname","fname","Student id","gender","email","phone","adress","dob","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("course",text="Course")
        self.student_table.heading("branch",text="Branch")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Id")
        self.student_table.heading("sname",text="Student name")
        self.student_table.heading("fname",text="Father name")
        self.student_table.heading("Student id",text="Student id")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("adress",text="Adress")
        self.student_table.heading("dob",text="Date of birth")
        self.student_table.heading("photo",text="PhotoSampleStatus")
  

        self.student_table["show"]="headings"

        self.student_table.column("course",width=100)
        self.student_table.column("branch",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("sname",width=100)
        self.student_table.column("fname",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("adress",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
       

       # validation
    # call back function
    # def checkname(self,name):
    #     if name.isalnum():
    #         return True
    #     if name=='':
    #         return True
    #     else:
    #         messagebox.showerror('invalid,"not allowed',+name[-1])
    # check student id
    def checkcontact(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return True
        else:
            messagebox.showerror('invalid,"not allowed') 
    # studentid
    def Student_id(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return True
        else:
            messagebox.showerror('invalid,"not allowed')             


    def validation(self):
        if self.var_sname.get()=='':
            messagebox.showerror("error",'please enter your name')
    # def checkemail(self,email):
    #     if len(email)>7:
    #         if re.match("^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,}$",email):
    #             return True
    #         else:
    #                 messagebox.showwarning('alert','invalid email example-sadiqali3-@gmail.com')
    #                 return False

    #     else:
    #         messagebox.showinfo("invalid",'enter email is too samll')

    
       # function declaration
    def add_data(self):
            if self.var_course.get()=="select course":
                messagebox.showerror("Error","select course",parent=self.root)

            elif self.var_branch.get()=="select Branch":
                messagebox.showerror("Error","Select branch",parent=self.root)

            elif self.var_year.get()=="select year":
                messagebox.showerror("Error","select year",parent=self.root)
            
            elif self.var_sem.get()=="Select Semester":
                messagebox.showerror("Error","select semester",parent=self.root)
            
            elif self.var_id.get()=='':
                messagebox.showerror("Error","please enter college generated unique id",parent=self.root)
           
            elif self.var_sname.get()=="":
                messagebox.showerror("Error","enter student name",parent=self.root)
            elif self.var_fname.get()=="":
                messagebox.showerror("Error","enter father name",parent=self.root)
            elif self.var_dob.get()=='':
                messagebox.showerror("Error","please enter this format eg:- 25/12/2021 ",parent=self.root)
            elif self.var_gender.get()=="select gender":
                messagebox.showerror("Error","select male or female",parent=self.root)
            elif self.var_email.get()=="":
                messagebox.showerror("Error","enter email",parent=self.root)
            # elif self.var_email.get()!=None:
            #     x=self.checkemail(self.var_email.get())

            





            elif len(self.var_phone.get())!=10:

                messagebox.showerror("Error","enter 10 digit phone number",parent=self.root)

            elif self.var_adress.get()=="":
                messagebox.showerror("Error","please enter adress",parent=self.root)
            elif self.var_sid.get()=="":
                messagebox.showerror("Error","enter Syudent_id",parent=self.root)
            


            else:
                    conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into studentdetails values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
		        																					self.var_course.get(),
																									self.var_branch.get(),
																									self.var_year.get(),
																									self.var_sem.get(),
																									self.var_id.get(),
																									self.var_sname.get(),
																									self.var_fname.get(),
																									self.var_sid.get(),
																									self.var_gender.get(),
																									self.var_email.get(),
																									self.var_phone.get(),
																									self.var_adress.get(),
                                                                                                    self.var_dob.get(),
																									
																									self.var_radio1.get()

																									))
                                                                                                                                                                                                        
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("succes","student details are succesfully added",parent=self.root)
                # except Exception as es:

                # # messagebox.showerror("error",f"due to :{str(es)}",parent=self.root)


        
    # fetch data
    def fetch_data(self):


        conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()			
        my_cursor.execute("select * from studentdetails")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())

            for i in data :
                self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()


         # ========get cursor==
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        


        self.var_course.set(data[0]),
        self.var_branch.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_sname.set(data[5]),
        self.var_fname.set(data[6]),
        self.var_sid.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_adress.set(data[11]),
        self.var_dob.set(data[12]),
        self.var_radio1.set(data[13])


    # update function
    def update_data(self):
        if self.var_course.get()=="select course" or self.var_sname.get()=="" or self.var_sid.get()=="":
            messagebox.showerror("Error","all field are required",parent=self.root)
        else:
            upadate=messagebox.askyesno("update","do u want to update this student details",parent=self.root)
            if upadate>0:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                # my_cursor.execute("update studentdetails set Course=%s, where Student_Id=%s",(
                #          self.var_course.get(),
                #         self.var_sid.get()
   
                # ))
                my_cursor.execute("update studentdetails set Course = %s, Branch = %s, Year = %s, Sem = %s,Student_Name = %s, Father_Name = %s,Student_Id=%s, Gender = %s, Email = %s, Phone = %s, Adress = %s,Dob = %s, PhotoSample = %s where Id=%s",(
                    
                                                                                                                                                    self.var_course.get(),
                                                                                                                                                    self.var_branch.get(),
                                                                                                                                                    self.var_year.get(),
                                                                                                                                                    self.var_sem.get(),																									                                                                                                                                                                                                                                                                                         self.var_sname.get(),
                                                                                                                                                    self.var_fname.get(),
                                                                                                                                                    self.var_sid.get(),
                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                    self.var_email.get(),
                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                    self.var_adress.get(),
                                                                                                                                                    self.var_dob.get(),																									
                                                                                                                                                    self.var_radio1.get() ,
                                                                                                                                                    self.var_id.get()                                                                                                                                                
                                                                                                                                                    

                                                                                                                                                                                

                ))

            else:
                if not upadate:
                    return
            messagebox.showinfo("success","Student details succesfully update succesfully",parent=self.root)                  
            conn.commit()
            self.fetch_data()
            conn.close()



      #delete function
    def delete_data(self):
        if self.var_sid.get()=="":
            messagebox.showerror("error","student id must required",parent=self.root)
        else:
            delete=messagebox.askyesno("student delete page","do u want to delete this student details",parent=self.root)
            if delete>0:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()			
                sql="delete from studentdetails where Student_Id=%s"
                val=(self.var_sid.get(),)
                my_cursor.execute(sql,val)
            else:
                if not delete:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()        
            messagebox.showinfo("Delete ","Succesfully  Deleted Student Details",parent=self.root)
            self.fetch_data()


    #reset data

    def reset_data(self):
        self.var_course.set("Select Course"),
        self.var_branch.set("Select Branch"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_id.set(""),
        self.var_sname.set(""),
        self.var_fname.set(""),
        self.var_sid.set(""),
        self.var_gender.set("select gender"),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_adress.set(""),
        self.var_dob.set(""),
        self.var_radio1.set("")
        



    # generate data set or take photo samples

    def generate_dataset(self):
        if self.var_course.get()=="select course" or self.var_sname.get()=="" or self.var_sid.get()=="":
            messagebox.showerror("Error","all field are required",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()	
            my_cursor.execute("select * from studentdetails")
            myresult=my_cursor.fetchall()
           
            id=0
            for x in myresult:
                id+=1
            my_cursor.execute("update studentdetails set Course = %s, Branch = %s, Year = %s, Sem = %s, id=%s,Student_Name = %s, Father_Name = %s,Student_Id=%s, Gender = %s, Email = %s, Phone = %s, Adress = %s,Dob = %s, PhotoSample = %s where id=%s",(
                                                                                        			self.var_course.get(),
																									self.var_branch.get(),
																									self.var_year.get(),
																									self.var_sem.get(),
                                                                                                    self.var_id.get(),
																								    self.var_sname.get(),
																									self.var_fname.get(),
                                                                                                    self.var_sid.get(),
																									
																									self.var_gender.get(),
																									self.var_email.get(),
																									self.var_phone.get(),
																									self.var_adress.get(),
                                                                                                    self.var_dob.get(),
																						
																									self.var_radio1.get(),
                                                                                                    self.var_sid.get()==id+1

                                                                             ))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()


                    # ===== load predefined data on face frontal from opencv                                                         
            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            

            def face_cropped(img):
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=face_classifier.detectMultiScale(gray,1.3,5)
                #scaling factor
                #minimum neighbour
                for (x,y,w,h) in faces:
                    face_cropped=img[y:y+h,x:x+w]
                    return face_cropped
            cap=cv2.VideoCapture(0)
            img_id=0
            while True:
                ret,my_frame=cap.read()
                if face_cropped(my_frame) is not None:
                    img_id+=1
                    face=cv2.resize(face_cropped(my_frame),(550,550))
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("cropped face",face)
                if cv2.waitKey(1)==13 or int(img_id)==50:
                    break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("result","generating data set succesfully")
                    
    # def  home(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Face_Recognition_System(self.new_window)

    








if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
