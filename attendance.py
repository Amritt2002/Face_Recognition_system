from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os
from datetime import datetime
from tkinter import filedialog
import pyttsx3
import csv
from csv import DictReader,DictWriter


mydata=[]
class Attendace:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Manage Attendance Management")
        self.root.config(bg="white")
        self.root.wm_iconbitmap("face.ico")

  
        # =============================== Variables===========================================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        # ===============Images==================================
        # img10 = Image.open("college_images/face_header_sd.jpg")
        # img10 = img10.resize((1530,100), Image.ANTIALIAS)
        # self.photoImg10 = ImageTk.PhotoImage(img10)
        # bg_lbl=Label(self.root,image=self.photoImg10)
        # bg_lbl.place(x=0,y=0,width=1530,height=100)
        
        img10 = Image.open("college_images/hqdefault.jpg")
        img10 = img10.resize((800,200), Image.ANTIALIAS)
        self.photoImg10 = ImageTk.PhotoImage(img10)
        bg_lbl=Label(self.root,image=self.photoImg10)
        bg_lbl.place(x=0,y=0,width=800,height=200)

        img11 = Image.open("college_images/AdobeStock_303989091.jpeg")
        img11 = img11.resize((800,200), Image.ANTIALIAS)
        self.photoImg11 = ImageTk.PhotoImage(img11)
        bg_lbl=Label(self.root,image=self.photoImg11)
        bg_lbl.place(x=800,y=0,width=800,height=200)

        img1 = Image.open("college_images/un.jpg")
        img1 = img1.resize((1535,710), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        bg_lbl=Label(self.root,image=self.photoImg1,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=200,width=1535,height=710)

        title=Label(self.root,text="STUDENT ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="crimson")
        title.place(x=0,y=150,width=1550,height=45)

        Manage_std_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        Manage_std_frame.place(x=15,y=10,width=1500,height=515)

        # myname=Label(self.root,text="Developed By:CodeWithKiran",fg="white",bg="black",font=("times new roman",18,"bold"))
        # myname.place(x=0,y=0)
        

        #  ================Left labelframe=================
        DataFrameLeft=LabelFrame(Manage_std_frame,bd=4,padx=2,relief=RIDGE,fg="crimson",bg="white",
                                                font=("arial",12,"bold"),text="Student Information ")
        DataFrameLeft.place(x=10,y=5,width=660,height=480)

        updateframe=Frame(DataFrameLeft,bd=2,relief=RIDGE,bg="white")
        updateframe.place(x=5,y=150,width=635,height=300)

        img30 = Image.open("college_images/face-recognition.png")
        img30 = img30.resize((650,150), Image.ANTIALIAS)
        self.photoImg30 = ImageTk.PhotoImage(img30)
        bg_lbl=Label(DataFrameLeft,image=self.photoImg30,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=0,width=650,height=150)

        empLabel=Label(updateframe,text="Student ID:",bg="white",font="comicsansns 11 bold")
        empLabel.grid(row=0,column=0,padx=4,pady=8)

        nameLabel=Label(updateframe,text="Roll:",bg="white",font="comicsansns 11 bold")
        nameLabel.grid(row=0,column=2,padx=4,pady=8)

        dateLabel=Label(updateframe,text="Name:",bg="white",font="comicsansns 11 bold")
        dateLabel.grid(row=1,column=0)

        dateLabel=Label(updateframe,text="Department:",bg="white",font="comicsansns 11 bold")
        dateLabel.grid(row=1,column=2)

        dateLabel=Label(updateframe,text="Time:",bg="white",font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=0)

        dateLabel=Label(updateframe,text="Date:",bg="white",font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2)

        attendanceLabel=Label(updateframe,text="Attendance Status",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)
        
        # ============================= Entry ====================================================
        self.atten_id=ttk.Entry(updateframe,textvariable=self.var_atten_id,width=22,font="comicsansns 11 bold")
        self.atten_id.grid(row=0,column=1,pady=8)
        self.atten_id.focus()

        atten_name=ttk.Entry(updateframe,textvariable=self.var_atten_roll,width=22,font="comicsansns 11 bold")
        atten_name.grid(row=0,column=3,pady=8)

        atten_date=ttk.Entry(updateframe,textvariable=self.var_atten_name,width=22,font="comicsansns 11 bold")
        atten_date.grid(row=1,column=1,pady=8)
        
        atten_date=ttk.Entry(updateframe,textvariable=self.var_atten_dep,width=22,font="comicsansns 11 bold")
        atten_date.grid(row=1,column=3,pady=8)
        
        atten_date=ttk.Entry(updateframe,textvariable=self.var_atten_time,width=22,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=1,pady=8)
        
        atten_date=ttk.Entry(updateframe,textvariable=self.var_atten_date,width=22,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=8)
        
        self.atten_status=ttk.Combobox(updateframe,width=22,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        ButtonFrame1=Frame(updateframe,bd=3,relief=RIDGE)
        ButtonFrame1.place(x=0,y=170,width=630,height=38)

        btnAddData=Button(ButtonFrame1,text="Import csv",command=self.importData,font=("arial",11,"bold"),width=16,bg="lime",fg="white")
        btnAddData.grid(row=0,column=0,padx=1)

        btnUpdate=Button(ButtonFrame1,text="Export csv",command=self.export_data,font=("arial",11,"bold"),width=16,bg="lime",fg="white")
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(ButtonFrame1,text="Update",command=self.action,font=("arial",11,"bold"),width=16,bg="lime",fg="white")
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(ButtonFrame1,text="Reset",command=self.clear,font=("arial",11,"bold"),width=16,bg="lime",fg="white")
        btnReset.grid(row=0,column=3,padx=1)

        #  ================Right labelframe=================
        DataFrameRight=LabelFrame(Manage_std_frame,bd=4,padx=2,relief=RIDGE,bg="white",fg="crimson",
                                                font=("arial",12,"bold"),text="Student Details")
        DataFrameRight.place(x=670,y=5,width=600,height=480)

        AttendanceFrame=Frame(DataFrameRight,bd=2,relief=RIDGE,bg="white")
        AttendanceFrame.place(x=5,y=5,width=500,height=400)

        # ===================== scroll bar ============================================
        scroll_x=ttk.Scrollbar(AttendanceFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(AttendanceFrame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(AttendanceFrame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Student ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"
    
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
         
        # self.csv_to_mysql()
        # self.fetch_data()
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cuesor)

    # ======back=========
        btnback=Button(title,text="Back",command=self.go_back,font=("arial",11,"bold"),width=17,bg="white",fg="red")
        btnback.pack(side=RIGHT)
    # back button
    def go_back(self):
        self.root.destroy()

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="facial_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_attendance")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in data:
                self.AttendanceReportTable.insert("",END,values=i)
            conn.commit()
        conn.close()

    

    # ======================= get Cursor ==============================================================
    def get_cuesor(self,event=""):
        cursor_rows=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_rows)
        row=content["values"]
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6])



    # ========================== fetch Data ===================================================================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    # # ============================ import CSV ===================================================================
    def importData(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            # mydata=[]
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)

    # export
    def export_data(self):
        try:
            if len (mydata) <1:
                messagebox.showerror("No Data","No Data to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open (fln,mode="w",newline="") as myfile:
                exp_writer=csv.writer(myfile,delimiter=",")
                for i in mydata:
                        exp_writer.writerow(i)
                messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    # export upadte
    def action(self):
        id=self.var_atten_id.get()
        roll=self.var_atten_roll.get()
        name=self.var_atten_name.get()
        dep=self.var_atten_dep.get()
        time=self.var_atten_time.get()
        date=self.var_atten_date.get()
        attendn=self.var_atten_attendance.get()

        # write to csv file
        try:
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="a",newline="\n") as f:
                dict_writer=DictWriter(f,fieldnames=(["ID","Roll","Name","Department","Time","Date","Attendance"]))
                dict_writer.writeheader()
                dict_writer.writerow({
                "ID":id,
                "Roll":roll,
                "Name":name,
                "Department":dep,
                "Time":time,
                "Date":date,
                "Attendance":attendn 
                    })
            messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #Clear Data
    def clear(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        self.atten_id.focus()


if __name__ == "__main__":
    root=Tk()
    obj=Attendace(root)
    root.mainloop()