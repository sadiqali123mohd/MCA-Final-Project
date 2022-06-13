from this import d
import cv2
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import os 

class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition ")
        title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        




        
        img_top=Image.open( "college images//facerecog.jpg")
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)


        
        # second image
        img_bottom=Image.open( "college images//facerecog.jpg")
        img_bottom=img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)
        #button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=450,width=200,height=40)
    
    def markAttendance(self,i,n,c,b):

        with open(r'C:\Users\sadiq\Desktop\face recognition software\attendance\mark.csv','r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
               
            if  ((i not in nameList)and (n not in nameList)and (c not in nameList)and (b not in nameList )): 
                now = datetime.now()
                time = now.strftime('%H:%M:%S')
                date = now.strftime('%d-%B-%Y') 
            # and (n not in nameList)and (c not in nameList)and (b not in nameList ))
                f.writelines(f'\n{i},{n},{c},{b},{time},{date}')


    # def mark_attendance(self,i,n,c,b):
    #     with open(r'D:\face recognition - Copy\attendance\mark.csv','r+') as f:
    #         myDataList = f.readlines()
    #         nameList = []
    #         for line in myDataList:
    #             entry = line.split(',')
    #             nameList.append(entry[0])
    #         if ((i not in nameList) and (n not in nameList)and (c not in nameList)and (b not in nameList)):
    #             now = datetime.now()
    #             time = now.strftime('%I:%M:%S:%p')
    #             date = now.strftime('%d-%B-%Y')
    #             f.writelines(f"\n{i},{n},{c},{b},{date},{time}")
    #             # f.writelines(f'n{i}{date}'{time})




    # def mark_attendance(self,i,n,c,b):
    #     with open("attendance.csv","r+",newline="\n") as f:
    #         mydatalist=f.readlines()
    #         name_list=[]
    #         for line in mydatalist:
    #             entry=line.split(" ")
    #             name_list.append(entry[0])
    #         if ((i not in name_list) and (n not in name_list) and (c not in name_list) and (b not in name_list)):
    #             now=datetime.now()
    #             d1=now.strftime("%d/%m/%y")
    #             dtString=now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{i},{n},{c},{b},{dtString},{d1}")



    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()


                my_cursor.execute("select Student_Id from studentdetails where id="+str(id))
                i=my_cursor.fetchone()
                i=''.join(i)

                my_cursor.execute("select Student_Name from studentdetails where id="+str(id))
                n=my_cursor.fetchone()
                n=''.join(n)

                my_cursor.execute("select Course from studentdetails where id="+str(id))
                c=my_cursor.fetchone()
                c=''.join(c)

                my_cursor.execute("select Branch from studentdetails where id="+str(id))
                b=my_cursor.fetchone()
                b=''.join(b)


                if confidence>75:
                    cv2.putText(img, f"S ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(110,255,255),3)
                    cv2.putText(img, f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Course:{c}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,255),3)
                    cv2.putText(img, f"Branch:{b}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.markAttendance(i,n,c,b)
                    # self.mark_attendance(i,n,)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            
        video_cap.release()
        cv2.destroyAllWindows()


if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()
