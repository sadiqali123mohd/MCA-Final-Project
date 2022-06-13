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
import csv


conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
cur = conn.cursor()

        #file = open('students.csv')
file = open(r'C:\Users\sadiq\Desktop\face recognition software\attendance\mark.csv')
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
    print("Exported succesfully")

    conn.commit()

    conn.close()
