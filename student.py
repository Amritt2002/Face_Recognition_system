from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os,random
from datetime import datetime
from tkinter import filedialog
import pyttsx3
import csv
import glob

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x730+0+0")
        self.root.title("Manage Employee Department")
        self.root.config(bg="white")
        self.root.wm_iconbitmap("face.ico")
        self.root.resizable(False,False)

        # variables
        self.ref_id=IntVar()
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


       
        # ===============Images==================================
        img10 = Image.open("college_images/stident_header.jpg")
        img10 = img10.resize((1300,70), Image.ANTIALIAS)
        self.photoImg10 = ImageTk.PhotoImage(img10)
        bg_lbl1=Label(self.root,image=self.photoImg10)
        bg_lbl1.place(x=0,y=0,width=1300,height=70)
        # img10 = Image.open("college_images/face-recognition.png")
        # img10 = img10.resize((400,130), Image.ANTIALIAS)
        # self.photoImg10 = ImageTk.PhotoImage(img10)
        # bg_lbl1=Label(self.root,image=self.photoImg10)
        # bg_lbl1.place(x=0,y=0,width=400,height=130)
        

        # img11 = Image.open("college_images/smart-attendance.jpg")
        # img11 = img11.resize((400,130), Image.ANTIALIAS)
        # self.photoImg11 = ImageTk.PhotoImage(img11)
        # bg_lbl2=Label(self.root,image=self.photoImg11)
        # bg_lbl2.place(x=400,y=0,width=400,height=130)

        # img13 = Image.open("college_images/iStock-182059956_18390_t12.jpg")
        # img13 = img13.resize((450,130), Image.ANTIALIAS)
        # self.photoImg13= ImageTk.PhotoImage(img13)
        # bg_lbl3=Label(self.root,image=self.photoImg13)
        # bg_lbl3.place(x=800,y=0,width=450,height=130)
       
        # ====================Background image==============================================
        # img1 = Image.open("college_images/university.jpg")
        # img1 = img1.resize((1250,710), Image.ANTIALIAS)
        # self.photoImg1 = ImageTk.PhotoImage(img1)
        # bg_lbl=Label(self.root,image=self.photoImg1,bd=2,relief=RIDGE)
        # bg_lbl.place(x=0,y=130,width=1535,height=710)

        Manage_std_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Manage_std_frame.place(x=0,y=90,width=1250,height=600)

        # ==================== Project title ==================================================
        title=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="crimson")
        title.place(x=0,y=60,width=1250,height=35)

        # myname=Label(self.root,text="Developed By:CodeWithKiran",fg="black",bg="white",font=("times new roman",18,"bold"))
        # myname.place(x=0,y=0)


        img_logo = Image.open("college_images/31-311346_oxford-university-logo.png")
        img_logo = img_logo.resize((50,50), Image.ANTIALIAS)
        self.photoImg_logo= ImageTk.PhotoImage(img_logo)
        bg_lbl5=Label(self.root,image=self.photoImg_logo,bd=20)
        bg_lbl5.place(x=200,y=60,width=50,height=40)

        # =================time================================
        def time(): 
            string = strftime('%H:%M:%S %p') 
            lbl.config(text = string) 
            lbl.after(1000, time) 
        
        lbl = Label(title, font = ('times new roman',16, 'bold'),background = 'white',foreground = 'blue') 
        lbl.place(x=0,y=(-15),width=120,height=50) 
        time()

        # =======Framedetails===================================================================================
        
        DataFrameLeft=LabelFrame(Manage_std_frame,bd=4,padx=2,relief=RIDGE,fg="crimson",bg="white",
                                                font=("arial",12,"bold"),text="Student Information ")
        DataFrameLeft.place(x=10,y=10,width=660,height=580)

        #  ================Right labelframe=================
        DataFrameRight=LabelFrame(Manage_std_frame,bd=4,padx=2,relief=RIDGE,bg="white",fg="crimson",
                                                font=("arial",12,"bold"),text="Student Details")
        DataFrameRight.place(x=670,y=10,width=600,height=580)

        img30 = Image.open("college_images/fml.jpg")
        img30 = img30.resize((650,120), Image.ANTIALIAS)
        self.photoImg30 = ImageTk.PhotoImage(img30)
        myimg=Label(DataFrameLeft,image=self.photoImg30,bd=2,relief=RIDGE)
        myimg.place(x=0,y=(-3),width=650,height=80)

        img20 = Image.open("college_images/iStock-1163542789-945x630.jpg")
        img20 = img20.resize((550,200), Image.ANTIALIAS)
        self.photoImg20 = ImageTk.PhotoImage(img20)
        bg_lbl=Label(DataFrameRight,image=self.photoImg20)
        bg_lbl.place(x=0,y=0,width=550,height=200)

        # ReferenceID
        referance_id=Label(myimg,font=("arial",12,"bold"),text="Reference  No:",bg="white")
        referance_id.place(x=0,y=53)

        txt_refid=ttk.Entry(myimg,textvariable=self.ref_id,width=8,font=("arial",12,"bold"),state=DISABLED)
        txt_refid.place(x=125,y=53)


        # Curent course Information labelFrame
        std_Info_label_frame=LabelFrame(DataFrameLeft,padx=10,bd=2,relief=RIDGE,font=("times new roman",11,"bold"),fg="darkgreen",bg="white",text="Current Course Information")
        std_Info_label_frame.place(x=1,y=80,width=650,height=115)

        # label and entries
        # department
       
        lbl_dep=Label(std_Info_label_frame,font=("arial",12,"bold"),text="Department:",bg="white")
        lbl_dep.grid(row=0,column=0,sticky=W,padx=2,pady=10)
        com_dep=ttk.Combobox(std_Info_label_frame,textvariable=self.var_dep,state="readonly",
                                                        font=("arial",12,"bold"),width=17)
        com_dep['value']=("Select Department","Computer","Mechnical","Civil","Electonic","Electrical","Automobile","IT")
        com_dep.current(0)
        com_dep.grid(row=0,column=1,sticky=W,padx=2)

        # course
        course_std=Label(std_Info_label_frame,font=("arial",12,"bold"),text="Courses:",bg="white")
        course_std.grid(row=0,column=2,sticky=W,padx=2,pady=10)

        com_txtcourse_std=ttk.Combobox(std_Info_label_frame,textvariable=self.var_course,state="readonly",
                                                        font=("arial",12,"bold"),width=17)
        com_txtcourse_std['value']=("Select Course","FE","SE","TE","BE")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0,column=3,sticky=W,padx=2,pady=10)

        # year
        currunt_year=Label(std_Info_label_frame,font=("arial",12,"bold"),text="Year:",bg="white")
        currunt_year.grid(row=1,column=0,sticky=W,padx=2,pady=10)

        com_txt_currunt_year=ttk.Combobox(std_Info_label_frame,textvariable=self.var_year,state="readonly",
                                                        font=("arial",12,"bold"),width=17)
        com_txt_currunt_year['value']=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        com_txt_currunt_year.current(0)
        com_txt_currunt_year.grid(row=1,column=1,sticky=W,padx=2)

        # semster
        label_Semester=Label(std_Info_label_frame,font=("arial",12,"bold"),text="Semester:",bg="white")
        label_Semester.grid(row=1,column=2,sticky=W,padx=2,pady=10)
        comSemester=ttk.Combobox(std_Info_label_frame,textvariable=self.var_semester,state="readonly",
                                                        font=("arial",12,"bold"),width=17)
        comSemester['value']=("Select Semester","Semster-1","Semester-2")
        comSemester.current(0)
        comSemester.grid(row=1,column=3,sticky=W,padx=2,pady=10)

        # student_class_Information
        std_personalData_label_frame=LabelFrame(DataFrameLeft,padx=10,pady=5,bd=2,relief=RIDGE,font=("times new roman",11,"bold"),fg="darkgreen",bg="white",text="Student Class Information")
        std_personalData_label_frame.place(x=1,y=195,width=650,height=260)

        lbl_id=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="StudentID No:",bg="white")
        lbl_id.grid(row=0,column=0,sticky=W,padx=2,pady=7)

        txt_id=ttk.Entry(std_personalData_label_frame,textvariable=self.va_std_id,width=22,font=("arial",11,"bold"))
        txt_id.grid(row=0,column=1,padx=2,pady=7)

        lbl_Name=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="Student Name:",bg="white")
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(std_personalData_label_frame,textvariable=self.var_std_name,width=22,font=("arial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        lbl_div=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="Class Division:",bg="white")
        lbl_div.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        com_txt_div=ttk.Combobox(std_personalData_label_frame,textvariable=self.var_div,state="readonly",
                                                        font=("arial",12,"bold"),width=18)
        com_txt_div['value']=("Select Division","A","B","C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        lbl_roll=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="Roll No:",bg="white")
        lbl_roll.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_roll=ttk.Entry(std_personalData_label_frame,textvariable=self.var_roll,width=22,font=("arial",11,"bold"))
        txt_roll.grid(row=1,column=3,padx=2,pady=7)

        lbl_gender=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="Gender:",bg="white")
        lbl_gender.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        com_txt_gender=ttk.Combobox(std_personalData_label_frame,textvariable=self.var_gender,state="readonly",
                                                        font=("arial",12,"bold"),width=18)
        com_txt_gender['value']=("Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        lbl_dob=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="DOB:",bg="white")
        lbl_dob.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(std_personalData_label_frame,textvariable=self.var_dob,width=22,font=("arial",11,"bold"))
        txt_dob.grid(row=2,column=3,padx=2,pady=7)

        lbl_email=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="Email:",bg="white")
        lbl_email.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_email=ttk.Entry(std_personalData_label_frame,textvariable=self.var_email,width=22,font=("arial",11,"bold"))
        txt_email.grid(row=3,column=1,padx=2,pady=7)

        lbl_phone=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="Phone No:",bg="white")
        lbl_phone.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(std_personalData_label_frame,textvariable=self.var_phone,width=22,font=("arial",11,"bold"))
        txt_phone.grid(row=3,column=3,padx=2,pady=7)

        lbl_adderss=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="Address:",bg="white")
        lbl_adderss.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_adderss=ttk.Entry(std_personalData_label_frame,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
        txt_adderss.grid(row=4,column=1,padx=2,pady=7)

        lbl_teacher=Label(std_personalData_label_frame,font=("arial",12,"bold"),text="Teacher Name:",bg="white")
        lbl_teacher.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        txt_teacher=ttk.Entry(std_personalData_label_frame,textvariable=self.var_teacher,width=22,font=("arial",11,"bold"))
        txt_teacher.grid(row=4,column=3,padx=2,pady=7)

        # radio buttons
        self.usertype=StringVar()
        radiobtn1=ttk.Radiobutton(std_personalData_label_frame, text="Take Photo Smaple", value="Yes", variable=self.usertype)
        radiobtn1.grid(row=5, column=0,pady=10)

        radiobtn2=ttk.Radiobutton(std_personalData_label_frame, text="No Photo Smaple", value="No", variable=self.usertype)
        radiobtn2.grid(row=5, column=1,pady=10)

        img30 = Image.open("college_images/iStock-182059956_18390_t12.jpg")
        img30 = img30.resize((320,70), Image.ANTIALIAS)
        self.photoImg50 = ImageTk.PhotoImage(img30)
        youimg=Label(std_personalData_label_frame,image=self.photoImg50,bd=2,relief=RIDGE)
        youimg.place(x=320,y=190,width=310,height=70)

        # ===========Buttonframe1================================================================================
        ButtonFrame1=Frame(DataFrameLeft,bd=3,relief=RIDGE)
        ButtonFrame1.place(x=0,y=450,width=650,height=38)

        ButtonFrame2=Frame(DataFrameLeft,bd=3,relief=RIDGE)
        ButtonFrame2.place(x=0,y=485,width=650,height=38)

        # ===================================ButtonFrame=====================================
        btnAddData=Button(ButtonFrame2,text="UPDATE",command=self.std_update,font=("arial",11,"bold"),width=23,bg="green",fg="white")
        btnAddData.grid(row=0,column=0,padx=1)

        btnUpdate=Button(ButtonFrame2,text="DELETE",command=self.std_delete,font=("arial",11,"bold"),width=23,bg="red",fg="white")
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(ButtonFrame2,text="RESET",command=self.clear,font=("arial",11,"bold"),width=23,bg="darkred",fg="white")
        btnDelete.grid(row=0,column=2,padx=1)

        # btnReset=Button(ButtonFrame2,text="RESET",command=self.clear,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        # btnReset.grid(row=0,column=3,padx=1)

        btnPhoto=Button(ButtonFrame1,text="SAVE STUDENT INFO/ADD PHOTO SAMPLE",command=self.generate_dataset,font=("arial",11,"bold"),width=72,bg="lime",fg="white")
        btnPhoto.grid(row=1,column=0,padx=1)

        # btnPhoto=Button(ButtonFrame1,text="UPDATE PHOTO SAMPLE",command=self.generate_dataset,font=("arial",11,"bold"),width=35,bg="blue",fg="white")
        # btnPhoto.grid(row=1,column=1,padx=1)

        # =======table&search=====================================================================================
        Table_frame=LabelFrame(DataFrameRight,text="View Student Details & Search System",font=("arial",11,"bold"),bg="white",bd=3,relief=RIDGE)
        Table_frame.place(x=0,y=200,width=570,height=70)

        # ==========Search By========
        lblSearch=Label(Table_frame,font=("arial",11,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=2,sticky=W,padx=5)

        # variable
        self.serch_var=StringVar()
        search_combo=ttk.Combobox(Table_frame,width=12,textvariable=self.serch_var,font=("times new roman",11),state="readonly")
        search_combo['values']=("Select Option","phone","roll","department")
        search_combo.grid(row=0,column=3,sticky=W,padx=5)
        search_combo.current(0)

        self.serchTxt_var=StringVar()
        txtSearch=ttk.Entry(Table_frame,width=16,textvariable=self.serchTxt_var,font=("times new roman",10))
        txtSearch.grid(row=0,column=4,padx=5)

        btnExit=Button(Table_frame,text="SEARCH",command=self.search_data,font=("arial",12,"bold"),width=10,bg="blue",fg="white")
        btnExit.grid(row=0,column=5,padx=5)

        btnExit=Button(Table_frame,text="SHOW ALL",command=self.fetch_data,font=("arial",12,"bold"),width=10,bg="blue",fg="white")
        btnExit.grid(row=0,column=6,padx=5)

        # =======Room Table Scrollbar=====================================================================================
        Table_frame=Frame(DataFrameRight,bd=4,relief=RIDGE)
        Table_frame.place(x=0,y=280,width=560,height=200)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_frame,column=("ref_id","dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo",
                                            )
                                            ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
       
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ref_id",text="Reference No")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Class Div")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher Name")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        
        self.student_table["show"]="headings"
        
        self.student_table.column("ref_id",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=120)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor_std)
        self.fetch_data()

        
        btnReset=Button(title,text="Back",command=self.go_back,font=("arial",11,"bold"),width=17,bg="white",fg="red")
        btnReset.pack(side=RIGHT)
    def go_back(self):
        self.root.destroy()
    # =============function declaration===================================
    def add_data(self):
        if (self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_roll.get()=="" or self.usertype.get()==""):
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="facial_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute('insert into new_student(id,department,course,year,semester,student_id,student_name,division,roll,gender,dob,email,phone,address,teacher_name,photo_sample ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                            id,
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.va_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.usertype.get()
                                                                                                                                                                                                           
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.clear()
                conn.close()
                engine=pyttsx3.init()
                # engine.setProperty('volume',2.0)
                voices = engine.getProperty('voices')       #getting details of current voice
                engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
                engine.say("Student has been added")
                engine.runAndWait()
                messagebox.showinfo("Suceess",f"Student has been added...!!!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    
    # ================================ photo sample============================
        
    def generate_dataset(self):
        if (self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_roll.get()=="" or self.usertype.get()==""):
            messagebox.showinfo("Result","Please provide complete details  of the user",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Test@123',database='facial_recognition')
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT * FROM new_student")
            myresult=my_cursor.fetchall()
            id=1
            for x in myresult:
                id+=1
            my_cursor.execute('insert into new_student(id,department,course,year,semester,student_id,student_name,division,roll,gender,dob,email,phone,address,teacher_name,photo_sample ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                            # self.ref_id.get(),
                                                                                                            id,
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.va_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.usertype.get()
                                                                                                                                                                                                           
                                                                                                            ))                                                                     
            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
      
            face_classified=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=face_classified.detectMultiScale(gray,1.3,5)
                # scaling factor=1.3
                # Minimum neighbor =5
                # if faces == ():
                #     return None
                for (x,y,h,w) in faces:
                    face_cropped=img[y:y+h,x:x+w]
                    return face_cropped
                    
            cap=cv2.VideoCapture(0)
            self.img_id=0
            while True:
                ret,frame=cap.read()
                if face_cropped(frame) is not None:
                    self.img_id +=1
                    face=cv2.resize(face_cropped(frame),(450,450))
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="collect_sample/user."+str(id)+"."+str(self.img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(self.img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(self.img_id)==100:
                        break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Generatig datasets completed!!!",parent=self.root)
    
    # ==========fetch data===============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="facial_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from new_student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ===========get cursor data=========
    def get_cursor_std(self,event=""):
        cursor_row_std=self.student_table.focus()
        content=self.student_table.item(cursor_row_std)
        data=content["values"]

        self.ref_id.set(data[0])
        self.var_dep.set(data[1]),
        self.var_course.set(data[2]),
        self.var_year.set(data[3]),
        self.var_semester.set(data[4]),
        self.va_std_id.set(data[5]),
        self.var_std_name.set(data[6]),
        self.var_div.set(data[7]),
        self.var_roll.set(data[8]),
        self.var_gender.set(data[9]),
        self.var_dob.set(data[10]),
        self.var_email.set(data[11]),
        self.var_phone.set(data[12]),
        self.var_address.set(data[13]),
        self.var_teacher.set(data[14]),
        self.usertype.set(data[15])

    def std_update(self):
        if (self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_roll.get()=="" or self.usertype.get()==""):
            messagebox.showwarning("Warning","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Success","Are you sure you want  to update this Student",parent=self.root) 
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="facial_recognition")
                    my_cursor=conn.cursor()
                    # my_cursor.execute("SELECT * FROM new_student where id=%s",(self.ref_id(),))
                    # id = my_cursor.fetchone()

                    my_cursor.execute("update new_student set department=%s,course=%s,year=%s,semester=%s,student_id=%s,student_name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher_name=%s,photo_sample=%s where id=%s",(
                                                                                                                        
                                                                                                                                                                            
                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                self.var_semester.get(), 
                                                                                                                                                                self.va_std_id.get(),                                                             
                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                self.usertype.get(),
                                                                                                                                                                self.ref_id.get()
                                                                                                                            
                                                                                                                                                                 ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student successfully update completed....!!!",parent=self.root)                                                                                                                   
                conn.commit()
                self.fetch_data()
                self.clear()
                conn.close()                                                                                                                                                                   
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def std_delete(self):
        if self.ref_id.get()== 0:
            messagebox.showerror("Error","Reference Id must be reqaired",parent=self.root)
        else:
            emp_delete=messagebox.askyesno("Facial Attendance Management System","Do you delete this student",parent=self.root)
            if emp_delete>0:
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="facial_recognition")
                my_cursor=conn.cursor()
                sql="delete from new_student where id=%s" 
                val=(self.ref_id.get(),)

                file_name_path="collect_sample"
                os.chdir=(file_name_path)
                # file_name_path="collect_sample/user."+str(id)+"."+str(self.img_id)+".jpg"

                # files=glob.glob("collect_sample/user."+str(id)+"."+str(self.img_id)+".jpg")
                files=glob.glob("user."+str(id))
                for i in files:
                    os.unlink(i)
                my_cursor.execute(sql,val)

            else:
                if not emp_delete:
                    return 
            # command=self.Manage_Emp
            # return

            conn.commit()
            conn.close()
            self.fetch_data()
            self.clear() 

    def clear(self):
        self.ref_id.set(0),
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.va_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.usertype.set("")

    def search_data(self):
        if self.serchTxt_var.get()=="" or self.serch_var.get()=="Select Option":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Test@123',database='facial_recognition')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from new_student where " +str(self.serch_var.get())+" LIKE '%"+str(self.serchTxt_var.get())+"%'")
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
