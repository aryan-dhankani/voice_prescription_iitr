from tkinter import *
from tkinter import filedialog
from tkinter import messagebox  
import prescription as pr
import speech_recognition as sr
import cv2
from PIL import Image,ImageTk
import pyttsx3
import os

os.environ["TCL_LIBRARY"] = "C:\\Users\\aryan\\AppData\\Local\\Programs\\Python\\Python37\\tcl\\tcl8.6"
os.environ["TK_LIBRARY"] = "C:\\Users\\aryan\\AppData\\Local\\Programs\\Python\\Python37\\tcl\\tk8.6"

window = Tk()
window.title("VOICE PRESCRIPTION")
window.iconbitmap("ICON vp.ico")
window.geometry("%dx%d+0+0" % (window.winfo_screenwidth()-300,window.winfo_screenheight()-50))
window.resizable(0,0)
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
r=sr.Recognizer()
def cv():
    img = cv2.cvtColor(pr.templete, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img,(int(img.shape[1]*(window.winfo_screenheight()/float(img.shape[0]))),window.winfo_screenheight() - 50))
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(image= img)
    image_frame.ImageTk = img
    image_frame.configure(image = img)
    showid = image_frame.after(10,show)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
r=sr.Recognizer()
   
left_frame = Frame(window)
image_frame = Label(left_frame)
image_frame.grid(row=0,column=0)
left_frame.grid()
middle_frame = Frame(window,width =0.700,highlightcolor='green',highlightbackground='green',highlightthickness=2,padx=15,pady=15,height=window.winfo_screenheight()-50)
def name():
        with sr.Microphone() as source:
                 
                speak("patient\'s name")
                try:
                        r.adjust_for_ambient_noise(source,duration=0.7)
                        audio = r.listen(source)
                        t1 = r.recognize_google(audio)
                        name_entry.insert(0,t1)
                        pr.name(name_entry.get())
                except:
                        speak(' could not recognize ')
name_label = Label(middle_frame,text="Name",font=("Comic Sans MS",15))
name_label.grid(row=1,column=0)
name_entry = Entry(middle_frame,width=50)
name_entry.grid(row=1,column=1)
b = Button(middle_frame, text="Name",bg='lightblue', command=name)
b.config(height=1,width=8,padx=5)
b.grid(row=1,column=5)
def age():
        with sr.Microphone() as source:
                 
                speak("patient\'s age")
                try:
                        r.adjust_for_ambient_noise(source,duration=0.7)
                        audio= r.listen(source)
                        t1 = r.recognize_google(audio)
                        age_entry.insert(0,t1)
                        pr.age(age_entry.get())
                except:
                        speak(' could not recognize ')
age_label = Label(middle_frame,text="Age",font=("Comic Sans MS",15))
age_label.grid(row=5,column=0)
age_entry = Entry(middle_frame,width=50)
age_entry.grid(row=5,column=1)
b1 = Button(middle_frame, text="Age",bg='lightblue', command=age)
b1.config( height=1, width=8, padx=5)
b1.grid(row=5,column=5)
def gender():
        with sr.Microphone() as source:
                speak("patient\'s gender")
                try:
                        r.adjust_for_ambient_noise(source,duration=0.7)
                        audio= r.listen(source)
                        t1 = r.recognize_google(audio)
                        if t1=='mail':
                            t1='Male'
                        gen_entry.insert(0,t1)
                        pr.gender(gen_entry.get())
                except:
                        speak(' could not recognize ')
gen_label = Label(middle_frame,text="Gender",font=("Comic Sans MS",15))
gen_label.grid(row=10,column=0)
gen_entry = Entry(middle_frame,width=50)
gen_entry.grid(row=10,column=1)
b2 = Button(middle_frame, text="Gender",bg='lightblue', command=gender)
b2.config( height=1, width=8, padx=5)
b2.grid(row=10,column=5)
def serial():
        with sr.Microphone() as source:
                 
                speak("patient\'s serial nmber")
                try:
                        r.adjust_for_ambient_noise(source,duration=0.7)
                        audio= r.listen(source)
                        t1 = r.recognize_google(audio)
                        sl_entry.insert(0,t1)
                        pr.serial(sl_entry.get())
                except:
                        speak(' could not recognize ')
sl_label = Label(middle_frame,text="Serial",font=("Comic Sans MS",15))
sl_label.grid(row=15,column=0)
sl_entry = Entry(middle_frame,width=50)
sl_entry.grid(row=15,column=1)
b3= Button(middle_frame, text="Serial",bg='lightblue', command=serial)
b3.config( height=1, width=8, padx=5)
b3.grid(row=15,column=5)
count=0
def medicines():
        global count
        with sr.Microphone() as source: 
                speak("patient\'s medicines")
                try:
                        count+=1
                        r.adjust_for_ambient_noise(source,duration=1)
                        audio= r.listen(source)
                        t1 = r.recognize_google(audio)
                        md_entry.insert(0,t1)
                        pr.medicine(count,t1,0,1)
                except:
                        speak(' could not recognize ')
md_label = Label(middle_frame,text="Medicines",font=("Comic Sans MS",15))
md_label.grid(row=20,column=0)
md_entry = Entry(middle_frame,width=50)
md_entry.grid(row=20,column=1)
##md1_label = Label(middle_frame,text="Qty ,ab(0 or 1) , time ",font=("Comic Sans MS",15))
##md1_label.grid(row=25,column=0)
##md1_entry = Entry(middle_frame,width=10)
##md1_entry.grid(row=25,column=3)
##md2_entry = Entry(middle_frame,width=10)
##md2_entry.grid(row=25,column=4)
##md3_entry = Entry(middle_frame,width=10)
##md3_entry.grid(row=25,column=5)
b4= Button(middle_frame, text="Medicines",bg='lightblue', command=medicines)
b4.config( height=1, width=8, padx=5)
b4.grid(row=20,column=5)
def symptoms():
        with sr.Microphone() as source:
                 
                speak("patient\'s symptoms")
                try:
                        r.adjust_for_ambient_noise(source,duration=0.7)
                        audio= r.listen(source)
                        t1 = r.recognize_google(audio)
                        sm_entry.insert(0,t1)
                        pr.symptoms(sm_entry.get())
                except:
                        speak(' could not recognize ')
sm_label = Label(middle_frame,text="Symptoms",font=("Comic Sans MS",15))
sm_label.grid(row=30,column=0)
sm_entry = Entry(middle_frame,width=50)
sm_entry.grid(row=30,column=1)
b5 = Button(middle_frame, text="Symptoms",bg='lightblue', command=symptoms)
b5.config( height=1, width=8, padx=5)
b5.grid(row=30,column=5)
def diag():
        with sr.Microphone() as source:
                 
                speak(" diagnosis ")
                try:
                        r.adjust_for_ambient_noise(source,duration=0.7)
                        audio= r.listen(source)
                        t1 = r.recognize_google(audio)
                        dia_entry.insert(0,t1)
                        pr.diagnosis(dia_entry.get())
                except:
                        speak(' could not recognize ')
dia_label = Label(middle_frame,text="Diagnosis",font=("Comic Sans MS",15))
dia_label.grid(row=35,column=0)
dia_entry = Entry(middle_frame,width=50)
dia_entry.grid(row=35,column=1)
b6 = Button(middle_frame, text="Diagnosis",bg='lightblue', command=diag)
b6.config( height=1, width=8, padx=5)
b6.grid(row=35,column=5)
def advice():
        with sr.Microphone() as source:
                 
                speak("advice for patient")
                try:
                        r.adjust_for_ambient_noise(source,duration=0.7)
                        audio= r.listen(source)
                        t1 = r.recognize_google(audio)
                        ad_entry.insert(0,t1)
                        pr.advice(ad_entry.get())
                except:
                        speak(' could not recognize ')
ad_label = Label(middle_frame,text="Advice",font=("Comic Sans MS",15))
ad_label.grid(row=40,column=0)
ad_entry = Entry(middle_frame,width=50)
ad_entry.grid(row=40,column=1)
b7 = Button(middle_frame, text="Advice",bg='lightblue', command=advice)
b7.config( height=1, width=8, padx=5)
b7.grid(row=40,column=5)
sig_label = Label(middle_frame,text="Signature",font=("Comic Sans MS",15))
sig_label.grid(row=45,column=0)
sig_entry = Entry(middle_frame,width=50)
sig_entry.grid(row=45,column=1)

def save():
        pr.save()
        messagebox.showinfo("information","saved at location : "+os.getcwd())
b8 = Button(middle_frame, text=" --- SAVE AS PDF --- ",bg='green', font=("Comic Sans MS",15), command=save)
b8.config( height = 2, width = 20)
b8.grid(row=50,column=1)

middle_frame.grid(row=0,column=2,stick=E)

def attachments():
    file_path = filedialog.askopenfilename()
    return file_path

def show():
    pr.name(name_entry.get())
    pr.age(age_entry.get())
    pr.gender(gen_entry.get())
    pr.serial(sl_entry.get())
    pr.medicine(0,md_entry.get(),'',0,1)
    pr.symptoms(sm_entry.get())
    pr.diagnosis(dia_entry.get())
    pr.advice(ad_entry.get())
    pr.signature(sig_entry.get())
    cv()
show()
def destroy():
    window.destroy()
menubar = Menu(window)
window.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="Exit", command=destroy)
window.mainloop()
