from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog
from tkcalendar import Calendar, DateEntry
import datetime
# myData = []
subject_code = ""
Date = ""
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student")
        self.sub = StringVar()
        
        # Background Cover
        img = Image.open(r"college images//detect.jpg")
        img = img.resize((1360,760),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        first_Label = Label(self.root, image = self.photoimg)
        first_Label.place(x = 0, y = 0, width = 1366, height = 768)

        title_label = Label(first_Label, text = "Student Management System", font = ("time new roman", 35,"bold"), bg = "#09194F", fg = "white")
        title_label.place(x = 0, y = 0, width = 1360, height = 45)

        home = Button(first_Label, text = "Home", command = root.destroy, cursor = "hand2", font = ("time new roman", 15,"bold"), bg = "cadetblue", fg = "white")
        home.place(x = 1150, y = 70, width = 100, height = 40)
        main_frame = Frame(first_Label, bd = 2, bg = "white",)
        main_frame.place(x = 90, y = 140, width = 1200, height = 500)

        
        # Right label form
        frame = Label(main_frame, bd = 2, bg = "white", relief = RIDGE, text = "Student Attendance", font = ("time new roman", 12))
        frame.place(x = 10, y = 10, width = 1150, height = 480)

        img_right = Image.open(r"college images//detect.jpg")
        img_right = img_right.resize((1150,120),Image.ANTIALIAS)

        self.photoimg_right = ImageTk.PhotoImage(img_right)
        right_Label = Label(frame, image = self.photoimg_right)
        right_Label.place(x = 0, y = 0, width = 1150, height = 120)
        
        # Table Frame

        table_frame = Frame(frame, bd = 2, bg = "white", relief = RIDGE)
        table_frame.place(x = 18, y = 130, width = 1100, height = 300)

        scroll_x = Scrollbar(table_frame, orient = HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient = VERTICAL)

        self.Attendance_table = ttk.Treeview(table_frame, columns = ("Student Id", "Roll No.", "Name", "Dept.", "Subject", "Time Slot", "Time", "Date", "Mark"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.Attendance_table.xview)
        scroll_y.config(command = self.Attendance_table.yview)

        self.Attendance_table.heading("Student Id", text = "Student Id")
        self.Attendance_table.heading("Roll No.", text = "Roll No.")
        self.Attendance_table.heading("Name", text = "Name")
        self.Attendance_table.heading("Dept.", text = "Dept.")
        self.Attendance_table.heading("Subject", text = "Subject")
        self.Attendance_table.heading("Time Slot", text = "Time Slot")
        self.Attendance_table.heading("Time", text = "Time")
        self.Attendance_table.heading("Date", text = "Date")
        self.Attendance_table.heading("Mark", text = "Mark")   

        self.Attendance_table["show"] = "headings"

        # Width of column
        self.Attendance_table.column("Student Id", width = 20)
        self.Attendance_table.column("Roll No.", width = 100)
        self.Attendance_table.column("Name", width = 150)
        self.Attendance_table.column("Dept.", width = 50)
        self.Attendance_table.column("Dept.", width = 50)
        self.Attendance_table.column("Subject", width = 100)
        self.Attendance_table.column("Time Slot", width = 50)
        self.Attendance_table.column("Time", width = 40)
        self.Attendance_table.column("Date", width = 50)
        self.Attendance_table.column("Mark", width = 70)

        self.Attendance_table.pack(fill = BOTH, expand = 1)


        Subject_Label = Label(frame, text = "Subject", font = ("time new roman", 12, "bold"), bg = "white")
        Subject_Label.place(x = 780, y = 435, width = 160, height = 35)

        Subject_Combo_Box = ttk.Combobox(frame, textvariable = self.sub, font = ("time new roman", 12, "bold"), state = "readonly", width = 16)
        Subject_Combo_Box["value"] = ("All","Data Analytics", "Internet of Things", "Machine Learning")
        Subject_Combo_Box.current(0)
        Subject_Combo_Box.place(x = 780, y = 435, width = 160, height = 35)


        Date = Button(frame, text = "Choose Date", command = self.date, width = 10, font = ("time new roman", 9, "bold"), bg = "cadetblue", fg = "White")
        Date.grid(row = 0, column = 0, padx = (650, 250), pady = 437)

        import_button = Button(frame, text = "Import", command = lambda: [self.add_data(), self.importCSV()], width = 8, font = ("time new roman", 12, "bold"), bg = "cadetblue", fg = "White")
        import_button.grid(row = 0, column = 1, padx = 10,pady = 437)

    def add_data(self):
        global subject_code
        subject_code = self.sub.get()

    def date(self):
        def print_sel():
            global Date
            dt = cal.selection_get()
            Date = dt.strftime("%d-%m-%Y")
            print(Date)

        top = Toplevel(self.root)

        cal = Calendar(top, font="Arial 14", selectmode='day', date_pattern="dd-mm-yyyy", cursor="hand1", day=12, month=5, year=2022)
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command = print_sel).pack()
  
    def fetch_data(self, rows):
        self.Attendance_table.delete(*self.Attendance_table.get_children())
        print(Date)
        for i in rows:         
            # print(Date)
            # print(i[7])
            if(i[4] == subject_code):
                self.Attendance_table.insert("", END, value = i)
            elif(subject_code == "All"):
                self.Attendance_table.insert("", END, value = i)
            # if(i[4] == subject_code and i[7] == Date):
            #     self.Attendance_table.insert("", END, value = i)
            # elif(subject_code == "All" and i[7] == Date):
            #     self.Attendance_table.insert("", END, value = i)
            # elif(subject_code == "All"):
            #     self.Attendance_table.insert("", END, value = i)
   

    def importCSV(self):


        # global myData
            myData = []

            fld = (r"D:\face recognition - Copy\attendance\mark.csv")
            with open(fld) as myfile: 
                csvread = csv.reader(myfile, delimiter = ",")

                for i in csvread:
                        myData.append(i)
                self.fetch_data(myData)

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
