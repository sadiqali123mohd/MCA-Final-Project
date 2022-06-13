from tkinter  import* 
from tkinter import ttk
from tkinter import scrolledtext
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os 
import numpy as np
class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")



        
        title_lbl=Label(self.root,text="Train Data",font=("times new roman",30,"bold"),bg="white",fg="BLACK")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        img_top=Image.open( "college images//detect.jpg")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)
        


        # button 
        b1_1=Button(self.root,text="Trian Data",command=self.train_classifier,cursor="hand2",font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)


        # second image
        img_top=Image.open( "college images//detect.jpg")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=0,y=440,width=1530,height=320)


    def train_classifier(self):
        
        data_path="data"
        path=[os.path.join(data_path,file) for file in os.listdir(data_path)]
        face=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')    # gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            face.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # print(ids)
        # print(face)


        ### train classifier and save

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(face,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("result","train datas set successfully")























if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
