from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class ChatBot: 
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot" )
        self.root.geometry("730x620+0+0")
        self.root.configure(bg="lightblue")
        # self.root.resizable(False,False)
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()

        img_chat=Image.open(r"college_images\chat.jpg")
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg_chat=ImageTk.PhotoImage(img_chat)


        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,image=self.photoimg_chat,compound=LEFT,text="CHAT ME",font=("arial",30,'bold'),fg='green',bg="white")
        # Title_label.grid(row=0,column=0,sticky=W)
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,yscrollcommand=self.scroll_y.set,width=65,height=20,bd=3,relief=RAISED,font=("arial",14))
        # self.text.grid(row=1,column=0,padx=2,sticky=W)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()
      
     
        btn_frame=Frame(self.root,bd=3,relief=RAISED,bg='white',width=730)
        btn_frame.pack()

        label=Label(btn_frame,text="Type Something",fg='green',bg='white',font=("arial",14))
        label.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.e=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=("times new roman",17))
        self.e.grid(row=0,column=1,padx=5,sticky="w")
        self.e.focus()

        self.send=Button(btn_frame,text="Send->>",command=self.send,width=8,bg="green",fg="white",font=("times new roman",16))
        self.send.grid(row=0,column=2,sticky=W)
        

        self.clear=Button(btn_frame,text="Clear Chat ",command=self.clear,width=8,bg="red",fg="white",font=("times new roman",15))
        self.clear.grid(row=1,column=0,sticky=W)
        
        self.msg=""
        self.label1=Label(btn_frame,text=self.msg,fg='red',bg='white',font=("arial",14))
        self.label1.grid(row=1,column=1,padx=5,sticky=W)

    #     self.engine=pyttsx3.init()
    #     self.engine.setProperty('volume',1.0)
    #     voices = self.engine.getProperty('voices')       #getting details of current voice
    #     self.engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

    # def speak(self,word):
    #     self.engine.say(word)
    #     self.engine.runAndWait()

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set("")

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set("")

    def send(self):
        send="\t\t\t"+"You: "+self.e.get()
        self.text.insert(END,"\n"+send)
        self.text.yview(END)

        if (self.e.get()==""):
            self.msg='Please enter some input'
            self.label1.config(text=self.msg,fg='red')
        else:
            self.msg=''
            self.label1.config(text=self.msg,fg='red')
            
        if (self.e.get()=="hello"):
            self.text.insert(END,"\n\n"+"Bot: Hi")
           

        elif (self.e.get()=="hi"):
            self.text.insert(END,"\n\n"+"Bot: Hello")

        elif (self.e.get()=="How are you?"):
            self.text.insert(END,"\n\n"+"Bot: fine and you")

        elif (self.e.get()=="Fantastic"):
            self.text.insert(END,"\n\n"+"Bot: Nice To Hear")

        elif (self.e.get()=="Who created you?"):
            self.text.insert(END,"\n\n"+"Bot: CodeWithKiran did using python")

        elif (self.e.get()=="What is your name?"):
            self.text.insert(END,"\n\n"+"Bot: My name is Mr. Hacker")
            
        elif (self.e.get()=="bye"):
            self.text.insert(END,"\n\n"+"Bot: Thank You For Chatting")

        elif (self.e.get()=="Can you speak Marathi"):
            self.text.insert(END,"\n\n"+"Bot: I'm still learning it..")

        elif (self.e.get()=="What is machine learning?"):
            self.text.insert(END,"\n\n"+"Bot: Machine learning is a branch\nof artificial intelligence (AI) focused\non building applications that learn\nfrom data and improve their accuracy\nover time without being programmed\nto do so. ")

        elif (self.e.get()=="How does face recognition work?"):
            self.text.insert(END,"\n\n"+"Bot: Facial recognition is a way of\nrecognizing a human face through\ntechnology. A facial recognition\nsystem uses biometrics to map\nfacial features from a photograph\nor video. It compares the information\nwith a database of known faces to find\na match")

        elif (self.e.get()=="How does facial recognition work step by step?"):
            self.text.insert(END,"\n\n"+"Bot:  Step 1: Face detection. The camera\ndetects and locates the image of a face,\neither alone or in a crowd. ...\nStep 2: Face analysis. Next, an image of\n the face is captured and analyzed. ...\nStep 3: Converting the image to data. ...\nStep 4: Finding a match.")
             
        elif (self.e.get()=="How many countries use facial recognition?"):
                self.text.insert(END,"\n\n"+"Bot: In Use	98\nApproved, but not implemented	12\nConsidering facial recognition technology	13\nNo evidence of use	68")
        
        elif (self.e.get()=="What is python programming?"):
                self.text.insert(END,"\n\n"+"Bot:Python is a general purpose\nand high level programming language.\nYou can use Python for developing\ndesktop GUI applications, websites\nand web applications. Also, Python,\nas a high level programming language")

        elif (self.e.get()=="What is chatbot?"):
            self.text.insert(END,"\n\n"+"Bot:A chatbot is a computer\nprogram that's designed to\nsimulate human conversation.")
                      
        else:
            self.text.insert(END,"\n\n"+"Bot: Sorry I dindn't get it")
        self.entry.set("")

        
if __name__ == '__main__':
    root=Tk()
    obj=ChatBot( root)
    root.mainloop()