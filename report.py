from tkinter  import* 
from tkinter import ttk
from tkinter import scrolledtext
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os 
import numpy as np
from tkinter import filedialog
class Report:
    def __init__(self,root):
        self.root=root



                                     

 
        self.root.geometry("1530x790+0+0")
        self.root.title("Report Generation System")

        title_lbl=Label(self.root,text="Report  ",font=("times new roman",30,"bold"),bg="white",fg="Blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        # MAIN FRAME
        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1530,height=650)
# LEFT FRAME
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=580)
# frame 
      
        btn_frame=Frame(main_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=160,width=580,height=95)
        #save button
        Btech_btn=Button(btn_frame,text="Btech",command=self.btech,width=15,font=("times new roman",12,"bold"),bg="green")
        Btech_btn.grid(row=0,column=0)

        #update
        MCA_btn=Button(btn_frame,text="MCA",command=self.mca,width=15,font=("times new roman",12,"bold"),bg="green")
        MCA_btn.grid(row=0,column=1)
        #delete
        Mtech_btn=Button(btn_frame,text="Mtech",command=self.mtech,width=15,font=("times new roman",12,"bold"),bg="green")
        Mtech_btn.grid(row=0,column=2)
        #reset
        MBA_btn=Button(btn_frame,text="MBA",command=self.mba,width=15,font=("times new roman",12,"bold"),bg="green")
        MBA_btn.grid(row=0,column=3)

        # export_csv_btn=Button(btn_frame,text="Export csv",width=15,command=self.exportCsv,font=("times new roman",12,"bold"),bg="green")
        # export_csv_btn.grid(row=1,column=1)
        
        Showall_csv_btn=Button(btn_frame,text="Show all",width=15,command=self.showall,font=("times new roman",12,"bold"),bg="green")
        Showall_csv_btn.grid(row=1,column=0)

        random_csv_btn=Button(btn_frame,text="Random pick student",width=15,command=self.random,font=("times new roman",12,"bold"),bg="green")
        random_csv_btn.grid(row=1,column=1)

        Punctual_btn=Button(btn_frame,text="Punctual student",width=15,command=self.punctual,font=("times new roman",12,"bold"),bg="green")
        Punctual_btn.grid(row=1,column=2)

        
        Defaulter_btn=Button(btn_frame,text="Defaulter student",width=15,command=self.defaulter,font=("times new roman",12,"bold"),bg="green")
        Defaulter_btn.grid(row=1,column=3)
        csvtomysql_btn=Button(btn_frame,text="csv to mysql student",width=15,command=self.csv,font=("times new roman",12,"bold"),bg="green")
        csvtomysql_btn.grid(row=2,column=0)

        # import_btn=Button(btn_frame,text="import new data",width=15,font=("times new roman",12,"bold"),bg="green")
        # import_btn.grid(row=2,column=0)

        # export_btn=Button(btn_frame,text="export data",width=15,font=("times new roman",12,"bold"),bg="green")
        # export_btn.grid(row=2,column=0)


        # button frame1
        # btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        # btn_frame1.place(x=0,y=190,width=650,height=35)
        # #take photo sample
        # takephoto_btn=Button(btn_frame1,text="Take Photo Sample",width=30,font=("times new roman",12,"bold"),bg="green")
        # takephoto_btn.grid(row=0,column=0)
        # # update photo sample 
        # takephoto_btn=Button(btn_frame1,text="Update photo sample",width=30,font=("times new roman",12,"bold"),bg="green")
        # takephoto_btn.grid(row=0,column=1)
        

        # right frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Report",font=("times new roman",12,"bold"))
        right_frame.place(x=666,y=10,width=660,height=580)
        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=70,width=700,height=300)

        # saveas_btn=Button(btn_frame,text="save as",width=15,command=self.punctual,font=("times new roman",12,"bold"),bg="green")
        # saveas_btn.grid(row=1,column=2)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("Student_id","Student_Name","Course","Branch","Date","Time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.xview)

        self.student_table.heading("Student_id",text="Student_id")
        self.student_table.heading("Student_Name",text="Student_Name")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Branch",text="Branch")
        self.student_table.heading("Date",text="Date")
        self.student_table.heading("Time",text="TIme")
        self.student_table["show"]="headings"

        
        
        self.student_table.column("Student_id",width=100)
        self.student_table.column("Student_Name",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Branch",width=100)
        self.student_table.column("Date",width=100)
        self.student_table.column("Time",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        

    def btech(self):


        conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()			
        my_cursor.execute("select DISTINCT  * from attendance where course='btech'")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())

            for i in data :
                self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()
    def showall(self):


        conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()			
        my_cursor.execute("select DISTINCT  * from attendance  ")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())

            for i in data :
                self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()
    
    def random(self):


        conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()			
        my_cursor.execute("select    * from attendance where time between '08:30:00' and '08:45:00' order by RAND() LIMIT 1  ")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())

            for i in data :
                self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()
    
    

    def defaulter(self):


        conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()			
        my_cursor.execute("select DISTINCT  * from attendance where  not time between '08:30:00' and '08:45:00'")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())

            for i in data :
                self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()
    def csv(self):
        import csv
        import mysql.connector

        conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")

        cur = conn.cursor()

        #file = open('students.csv')
        file = open(r'C:\Users\sadiq\Desktop\face recognition software\attendance/mark.csv')
        csv_data = csv.reader(file)

        skipHeader = True

        for row in csv_data:
            if skipHeader:
                skipHeader = False
                continue
            cur.execute('INSERT INTO attendance(Student_id, Student_name,Course,Branch,Date,Time)' 'VALUES(%s,%s, %s, %s, %s, %s)', row)

        #query = "LOAD DATA INFILE 'C:/python/python-insert-csv-data-into-mysql/students-header.csv' INTO TABLE student FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (student_id, student_name, student_dob, student_email, student_address)"
        # D:\Knowledge_Gate java projects\face recognition - Copy
        query = r"LOAD DATA INFILE 'C:\Users\sadiq\Desktop\face recognition software\attendance/mark.csv' INTO TABLE attendance FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' (Student_id, Student_name,Course,Branch,Date,Time)"

        cur.execute(query)
        messagebox.showinfo("sucess","exported csv succesfully",parent=self.root)

        conn.commit()

        conn.close()


    def punctual(self):


        conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()			
        my_cursor.execute("select  DISTINCT * from attendance where time between '08:30:00' and '08:45:00'")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())

            for i in data :
                self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()
    
    
    def mca(self):


        conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()			
        my_cursor.execute("select DISTINCT  * from attendance where course='mca'")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())

            for i in data :
                self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()
    def mtech(self):


        conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()			
        my_cursor.execute("select * from attendance where course='mtech'")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())

            for i in data :
                self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()
    def mba(self):


        conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()			
        my_cursor.execute("select DISTINCT  * from attendance where course='mba'")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())

            for i in data :
                self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()

    def exportCsv(self):
            if len(data)<1:
                messagebox.showerror("no data ","no data found",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                    exp_write=csv.writer(myfile,delimiter=",")
                    for i in data:
                            exp_write.writerow(i)
                    messagebox.showinfo("data export","data are exported succesfull"+os.path.basename(fln)+"succesfully")


       




if __name__=="__main__":
    root=Tk()
    obj=Report(root)
    root.mainloop()