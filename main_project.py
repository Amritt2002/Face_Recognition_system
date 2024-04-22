from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import os
from tkinter import messagebox
from student import Student
from train import Train_Data
from recognition_face import Recognition_Face
from attendance import Attendace
from developer import Developer
from my_first_chatbot import ChatBot

# ***************************************** Main Window *****************************************************
# def main():
#     win=Tk()
#     app=FaceRecognitionSystem(win)
#     win.mainloop()
# ====================================== First Window =======================================================
class FaceRecognitionSystem:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        # self.root.resizable(False,False)
        self.root.title("Face Recognition Attendance System")
        self.root.wm_iconbitmap("face.ico")

        # ===============Images==================================
        img10 = Image.open("college_images/face_header_sd.jpg")
        img10 = img10.resize((1530,100), Image.ANTIALIAS)
        self.photoImg10 = ImageTk.PhotoImage(img10)
        bg_lbl=Label(self.root,image=self.photoImg10)
        bg_lbl.place(x=0,y=0,width=1530,height=100)

        # img10 = Image.open("college_images//BestFacialRecognition.jpg")
        # img10 = img10.resize((500,100), Image.ANTIALIAS)
        # self.photoImg10 = ImageTk.PhotoImage(img10)
        # bg_lbl=Label(self.root,image=self.photoImg10)
        # bg_lbl.place(x=0,y=0,width=500,height=100)

        # img11 = Image.open("college_images/facialrecognition.png")
        # img11 = img11.resize((500,100), Image.ANTIALIAS)
        # self.photoImg11 = ImageTk.PhotoImage(img11)
        # bg_lbl=Label(self.root,image=self.photoImg11)
        # bg_lbl.place(x=500,y=0,width=500,height=100)

        # img13 = Image.open("college_images/images.jpg")
        # img13 = img13.resize((550,100), Image.ANTIALIAS)
        # self.photoImg13= ImageTk.PhotoImage(img13)
        # bg_lbl=Label(self.root,image=self.photoImg13)
        # bg_lbl.place(x=1000,y=0,width=550,height=100)

        # logot=Button(bg_lbl,bd=2,text="User Logout",cursor="hand2",command=self.Logout,font=("times new roman",14,"bold"),bg="white",fg="red")
        # logot.place(x=410,y=0)

        # ====================Background image==============================================
        img1 = Image.open("college_images/bg11.jpg")
        img1 = img1.resize((1600,710), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        bg_lbl=Label(self.root,image=self.photoImg1)
        bg_lbl.place(x=0,y=100,width=1600,height=710)

        # ==================== Project title ==================================================
        title=Label(bg_lbl,text="FACE RECOGNITION ATTENDACE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="darkblue")
        title.place(x=0,y=(-2),width=1540,height=45)

        # ==================== Project buttom(description) ==================================================
        downtitle=Label(self.root,text="Leadership is the ability to facilitate movement in the needed direction and have people feel good about it",font=("times new roman",20,"bold"),bd=2,relief=RAISED,bg="white",fg="red")
        downtitle.place(x=0,y=765,width=1600,height=35)

        # =================time================================
        def time(): 
            string = strftime('%H:%M:%S %p') 
            lbl.config(text = string) 
            lbl.after(1000, time) 
        
        lbl = Label(title, font = ('times new roman',14, 'bold'),background = 'white',foreground = 'blue') 
        lbl.place(x=0,y=(-15),width=110,height=50) 
        time() 

        # myname=Label(self.root,text="Developed By:CodeWithKiran",fg="white",bg="black",font=("times new roman",18,"bold"))
        # myname.place(x=0,y=0)

        # ==================Employee Department Button ===========================================
        
        img2 = Image.open("college_images/fml.jpg")
        img2 = img2.resize((220,220), Image.ANTIALIAS)
        self.photoImg2 =  ImageTk.PhotoImage(img2)
        self.b2 =Button(self.root,image=self.photoImg2,command=self.Manage_Emp,borderwidth=2,fg="red", width=220,cursor="hand2")
        self.b2.place(x=200,y=180,width=220,height=220)

        # photo_label=Button(self.root,text="Student Details",borderwidth=15,command=self.detect_window,cursor="hand2",font="comicsansns 15 bold",fg="white",bg="darkblue")
        # photo_label.place(x=200,y=380,width=220)

        b3 =Button(self.root,text="STUDENT DETAILS",borderwidth=5,font="comicsansns 15 bold",bg="#0AFFFF",fg="white",cursor="hand2")
        b3.place(x=199,y=380,width=220,height=40)

        # myname=Label(self.root,text="Developed By:CodeWithKiran",fg="white",bg="black",font=("times new roman",18,"bold"))
        # myname.place(x=0,y=0)


        # ==================Train Button ===========================================
        img3 = Image.open("college_images/di.jpg")
        img3 = img3.resize((220,220), Image.ANTIALIAS)
        self.photoImg3 =  ImageTk.PhotoImage(img3)
        b3 =Button(self.root,image=self.photoImg3,text="Face Detector",command=self.train_window,bd=2,relief=SUNKEN,font=("times new roman",22,"bold"),fg="white", width=220,cursor="hand2")
        b3.place(x=200,y=460,width=220,height=220)

        photo_label=Button(self.root,text="TRAIN DATA",command=self.train_window,cursor="hand2",borderwidth=8,font="comicsansns 15 bold",bg="#E2F516",fg="white")
        photo_label.place(x=200,y=660,width=222,height=40)

        # ==================Face Detector Button ===========================================
        img = Image.open("college_images/IMG_1183_augmented_reality_faces1.jpg")
        img = img.resize((220,220), Image.ANTIALIAS)
        self. photoImg =  ImageTk.PhotoImage(img)
        b1 =Button(self.root,image=self.photoImg,text="FACE DETECTOR",command=self.detect_window,bd=2,relief=SUNKEN,font=("times new roman",22,"bold"),fg="lime", width=220,cursor="hand2")
        b1.place(x=500,y=180,width=220,height=220)

        face_label=Button(self.root,text="FACE RECOGNITION",command=self.detect_window,cursor="hand2",bd=8,font="comicsansns 15 bold",fg="white",bg="#7D0552")
        face_label.place(x=500,y=380,width=222,height=40)

        # ==================Sample Image Button ===========================================
        img4 = Image.open("college_images/teaser.png")
        img4 = img4.resize((220,220), Image.ANTIALIAS)
        self.photoImg4 =  ImageTk.PhotoImage(img4)
        b4 =Button(self.root,image=self.photoImg4,text="Photo",command=self.open_photo,font=("times new roman",22,"bold"),bd=2,relief=SUNKEN,fg="white", width=220,cursor="hand2")
        b4.place(x=500,y=460,width=220,height=220)

        photo_label=Button(self.root,text="PHOTOS",command=self.open_photo,borderwidth=5,cursor="hand2",font="comicsansns 15 bold",fg="white",bg="#FF1493")
        photo_label.place(x=500,y=660,width=222,height=40)

        # ==================Attendace report Button ===========================================
        img5 = Image.open("college_images/facial_0.jpeg")
        img5 = img5.resize((220,220), Image.ANTIALIAS)
        self.photoImg5 =  ImageTk.PhotoImage(img5)
        b5 =Button(self.root,image=self.photoImg5,command=self.attendance_report,text="Attendance Report",bd=2,relief=SUNKEN,font=("times new roman",22,"bold"),fg="red", width=220,cursor="hand2")
        b5.place(x=800,y=180,width=220,height=220)

        photo_label=Button(self.root,text="ATTENDANCE",borderwidth=5,command=self.attendance_report,cursor="hand2",font="comicsansns 15 bold",fg="white",bg="#6A0DAD")
        photo_label.place(x=800,y=380,width=220,height=40)

        # ==================Chat Bot Button ===========================================
        img6 = Image.open("college_images/chat.jpg")
        img6 = img6.resize((220,220), Image.ANTIALIAS)
        self.photoImg6 =  ImageTk.PhotoImage(img6)
        b6 =Button(self.root,image=self.photoImg6,command=self.help_window,font=("times new roman",22,"bold"),bd=2,relief=SUNKEN,fg="white", width=220,cursor="hand2")
        b6.place(x=1100,y=180,width=220,height=220)

        photo_label=Button(self.root,text="CHATBOT",command=self.help_window,borderwidth=5,cursor="hand2",font="comicsansns 15 bold",fg="white",bg="darkblue")
        photo_label.place(x=1100,y=380,width=220,height=40)

        # ==================Developer Image Button ===========================================
        img7 = Image.open("college_images/iStock-1163542789-945x630.jpg")
        img7 = img7.resize((220,220), Image.ANTIALIAS)
        self.photoImg7 =  ImageTk.PhotoImage(img7)
        b7 =Button(self.root,image=self.photoImg7,text="Photo",command=self.developer_window,font=("times new roman",22,"bold"),bd=2,relief=SUNKEN,fg="white", width=220,cursor="hand2")
        b7.place(x=800,y=460,width=220,height=220)

        photo_label=Button(self.root,text="DEVELOPER",command=self.developer_window,borderwidth=5,cursor="hand2",font="comicsansns 15 bold",fg="white",bg="darkgreen")
        photo_label.place(x=800,y=660,width=220,height=40)

        # ==================Exit Image Button ===========================================
        img8 = Image.open("college_images/1200px-Glass_exit_sign.jpg")
        img8 = img8.resize((220,220), Image.ANTIALIAS)
        self.photoImg8 =  ImageTk.PhotoImage(img8)
        b8 =Button(self.root,image=self.photoImg8,command=self.iExit,text="Photo",font=("times new roman",22,"bold"),bd=2,relief=SUNKEN,fg="white", width=220,cursor="hand2")
        b8.place(x=1100,y=460,width=220,height=220)

        photo_label=Button(self.root,text="EXIT",command=self.iExit,borderwidth=5,cursor="hand2",font="comicsansns 15 bold",fg="white",bg="red")
        photo_label.place(x=1100,y=660,width=220,height=40)

    def Logout(self):
        self.root.destroy()

    # ================== Exit function =======================================================================
    def iExit(self):
        self.iExit=messagebox.askyesno("Face Detector System","Confirm you want to exit",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

    def open_photo(self):
        os.startfile("collect_sample")

  
# # ============================================ Another window fuctions ========================================
    def Manage_Emp(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def attendance_report(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendace(self.new_window)

    def train_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Train_Data(self.new_window)  

    def detect_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Recognition_Face(self.new_window) 

    def developer_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)   


    def help_window(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)     
  

# if __name__ == "__main__":
#     main()

if __name__ == '__main__':
    root=Tk()
    obj=FaceRecognitionSystem(root)
    root.mainloop()
    
 
  


   



