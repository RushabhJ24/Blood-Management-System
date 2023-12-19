from tkinter import *
import sqlite3
from PIL import Image, ImageTk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox

conn=sqlite3.connect('donation_form.db')



def changeToReg():
    mainFrame.forget()
    contactFrame.forget()
    aboutFrame.forget()
    donorFrame.forget()
    regFrame.pack(fill=BOTH,expand=True)

def changeToMain():
    regFrame.forget()
    contactFrame.forget()
    aboutFrame.forget()
    donorFrame.forget()
    seaBldGrpFrame.forget()
    mainFrame.pack(fill=BOTH,expand=True)
   
def changeToContact():
    mainFrame.forget()
    regFrame.forget()
    aboutFrame.forget()
    donorFrame.forget()
    seaBldGrpFrame.forget()
    contactFrame.pack(fill=BOTH,expand=True)
    
def changeToAbout():
    mainFrame.forget()
    regFrame.forget()
    contactFrame.forget()
    donorFrame.forget()
    seaBldGrpFrame.forget()
    aboutFrame.pack(fill=BOTH,expand=True)

def changeToDonor():
    mainFrame.forget()
    regFrame.forget()
    contactFrame.forget()
    aboutFrame.forget()
    seaBldGrpFrame.forget()
    donorFrame.pack(fill=BOTH,expand=True)

def changeToSearch():
    mainFrame.forget()
    regFrame.forget()
    contactFrame.forget()
    aboutFrame.forget()
    donorFrame.forget()
    seaBldGrpFrame.pack(fill=BOTH,expand=True)

def reg():
  try:
   cursor=conn.cursor()
   name=e1.get()
   valu=radio.get()
   if(valu==1):
       gender="Male"
   else:
       gender="Female"
   dob=cal.get()
   bgrp=clicked.get()
   mobno=e2.get()
   email=e3.get()
   add=e4.get()
   weight=e5.get()
   pulse=e6.get()
   temp=e9.get()
   hb=e7.get()
   bp=e8.get()
   value=radio1.get()
   if(value==3):
      prevdonate="Yes"
   else:
      prevdonate="No"
   disease=e10.get()
   cursor.execute("INSERT INTO details VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(name,gender,dob,bgrp,mobno,email,add,weight,pulse,temp,hb,bp,prevdonate,disease))
   conn.commit()
   messagebox.showinfo("Status","Details Recorded")
   e1.delete(0,END)
   e2.delete(0,END)
   e3.delete(0,END)
   e4.delete(0,END)
   e5.delete(0,END)
   e6.delete(0,END)
   e7.delete(0,END)
   e8.delete(0,END)
   e10.delete(0,END)
   e9.delete(0,END)

  except:
   messagebox.showinfo("Status","Error Occured")   

#Main Window
root=Tk()
root.geometry("1200x650")
root.title("BLOOD MANAGEMENT SYSTEM")

#About Us Frame
aboutFrame=Frame(root)
Label(aboutFrame,text="About Us",font=('aria',19,'bold')).place(x=30,y=50)
ph=Image.open("aboutus.jpg")
re=ph.resize((100,100))
im=ImageTk.PhotoImage(re,master=aboutFrame)
lab=Label(aboutFrame,image=im)
lab.place(x=50,y=100)
lab.image=im
Label(aboutFrame,text="PCE BLOOD MANAGEMENT SYSTEM",font=('aria',26,'bold'),fg="Red").place(x=350,y=100)
l4=Label(aboutFrame,text="""Our Project “Blood Bank Management System” is a computerized system used to store  and  retrieve
information related to Blood donations/inventory the project aims to expose the relevance and
importance of Blood Management Systems. The system allows the admin/receptionist to store and
retrieve information like blood donor details, blood receiver details, amount of blood present
in the inventory of the blood bank store, etc.The Blood Bank Management System checks for the
availability of a certain blood type like A+, A-, B+, B- etc.""",font=('aria',16))
l4.place(x=180,y=180)
l5=Label(aboutFrame,text=""" Blood Bank Management System is designed to store, process, retrieve and analyze information
concerned with the administrative and management in a blood bank. This project aims at maintaining all the
information pertaining to blood donors, different blood groups available in each blood bank and helps them
manage in a better way. The main Aim is to utilize the resources in a better way.""",font=('aria',16))
l5.place(x=180,y=380)

#Search Blood Group Frame
seaBldGrpFrame=Frame(root)    
Label(seaBldGrpFrame,text="Enter City",font=('Times',16)).place(x=250,y=50)
Label(seaBldGrpFrame,text="Select Blood Group",font=('Times',16)).place(x=250,y=100)
er1=Entry(seaBldGrpFrame)
er1.place(x=450,y=50)
label=Label(seaBldGrpFrame)    
options=['Select Blood Group','A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
clicked2=StringVar()
clicked2.set("Select Blood Group")
drop=OptionMenu(seaBldGrpFrame,clicked2,*options).place(x=450,y=100)

def searchbgrp():
    try:
        address=er1.get()
        bgrp=clicked2.get()
        Label(seaBldGrpFrame,text='Name',font=('aria',16,'bold')).place(x=200,y=200)
        Label(seaBldGrpFrame,text='Mobile No.',font=('aria',16,'bold')).place(x=450,y=200)
        Label(seaBldGrpFrame,text='Email',font=('aria',16,'bold')).place(x=600,y=200)
        Label(seaBldGrpFrame,text='Gender',font=('aria',16,'bold')).place(x=900,y=200)
        cursor.execute("SELECT * from details where bloodgrp=?",(bgrp,))
        output=cursor.fetchall()
        showdata=""
        j=0
        for i in output:
            if address==i[6]:
                Label(seaBldGrpFrame,text=i[0],font=('aria',16)).place(x=200,y=240+j)
                Label(seaBldGrpFrame,text=i[4],font=('aria',16)).place(x=450,y=240+j)
                Label(seaBldGrpFrame,text=i[5],font=('aria',16)).place(x=600,y=240+j)
                Label(seaBldGrpFrame,text=i[1],font=('aria',16)).place(x=900,y=240+j)
                j=j+40
    except:
        messagebox.showinfo("Status","Invalid User")
            
        
        
Button(seaBldGrpFrame,text="Search",fg='Green',bg='White',command=searchbgrp,font=('Times',18)).place(x=700,y=70)

#Donor Frame
donorFrame=Frame(root)
cursor=conn.cursor()
Label(donorFrame,text="Email",font=('Times',18,'bold')).place(x=350,y=100)
Label(donorFrame,text="Password",font=('Times',18,'bold')).place(x=350,y=150)
Label(donorFrame,text="Your password is your DOB as MM/DD/YY",font=('Times',11)).place(x=350,y=180)
ph=Image.open("login.jpg")
re=ph.resize((200,200))
im=ImageTk.PhotoImage(re,master=donorFrame)
lab=Label(donorFrame,image=im)
lab.place(x=100,y=30)
lab.image=im
le1=Entry(donorFrame)
le1.place(x=550,y=100)
le2=Entry(donorFrame,show='*')
le2.place(x=550,y=150)
def login():
   try:
           username=le1.get()
           password=(le2.get())
           cursor.execute("SELECT * from details where email=?",(username,))
           output=cursor.fetchall()
           showdata=""
           for i in output:
            if password==i[2]:
                    messagebox.showinfo("Status","Welcome")
                    d1=Label(donorFrame,text='Donor Details',font=('aria',18,'bold'))
                    d1.place(x=260,y=250)
                    d2=Label(donorFrame,text='Name',font=('aria',14))
                    d2.place(x=50,y=300)
                    d3=Label(donorFrame,text='Gender',font=('aria',14))
                    d3.place(x=350,y=300)
                    d4=Label(donorFrame,text='Date Of Birth',font=('aria',14))
                    d4.place(x=50,y=340)    
                    d5=Label(donorFrame,text='Blood Group',font=('aria',14))
                    d5.place(x=350,y=340)
                    d6=Label(donorFrame,text='Contact No.',font=('aria',14))
                    d6.place(x=50,y=380)
                    d7=Label(donorFrame,text='Email',font=('aria',14))
                    d7.place(x=350,y=380)
                    d8=Label(donorFrame,text='Address',font=('aria',14))
                    d8.place(x=50,y=420)
                    d9=Label(donorFrame,text='Weight',font=('aria',14))
                    d9.place(x=350,y=420)
                    d10=Label(donorFrame,text='Pulse',font=('aria',14))
                    d10.place(x=50,y=460)
                    d11=Label(donorFrame,text='Hb',font=('aria',14))
                    d11.place(x=350,y=460)
                    d12=Label(donorFrame,text='BP',font=('aria',14))
                    d12.place(x=50,y=500)
                    d13=Label(donorFrame,text='Temperature',font=('aria',14))
                    d13.place(x=350,y=500)
                    d14=Label(donorFrame,text='Have you donated previously?',font=('aria',14))
                    d14.place(x=50,y=540)
                    d15=Label(donorFrame,text=' Any disease(s)',font=('aria',14))
                    d15.place(x=50,y=580)
                    Label(donorFrame,text=i[0],font=('Times',14)).place(x=200,y=300)
                    Label(donorFrame,text=i[1],font=('Times',14)).place(x=500,y=300)
                    Label(donorFrame,text=i[2],font=('Times',14)).place(x=200,y=340)
                    Label(donorFrame,text=i[3],font=('Times',14)).place(x=500,y=340)
                    Label(donorFrame,text=i[4],font=('Times',14)).place(x=200,y=380)
                    Label(donorFrame,text=i[5],font=('Times',14)).place(x=500,y=380)
                    Label(donorFrame,text=i[6],font=('Times',14)).place(x=200,y=420)
                    Label(donorFrame,text=i[7],font=('Times',14)).place(x=500,y=420)
                    Label(donorFrame,text=i[8],font=('Times',14)).place(x=200,y=460)
                    Label(donorFrame,text=i[10],font=('Times',14)).place(x=500,y=460)
                    Label(donorFrame,text=i[11],font=('Times',14)).place(x=200,y=500)
                    Label(donorFrame,text=i[9],font=('Times',14)).place(x=500,y=500)
                    Label(donorFrame,text=i[12],font=('Times',14)).place(x=350,y=540)
                    Label(donorFrame,text=i[13],font=('Times',14)).place(x=350,y=580)
                    
                    d16=Label(donorFrame,text='About Donation',font=('aria',18,'bold'))
                    d16.place(x=800,y=250)
                    
                    if(i[12]=='Yes'):
                        d17=Label(donorFrame,text='When was the last time you Donated ?',font=('aria',14))
                        d17.place(x=700,y=300)
                        cal=DateEntry(donorFrame,width=18,year=2004,month=1,day=1,background='navyblue',fg='white',borderwidth=2)
                        cal.place(x=700,y=340)
                        cal1=str(cal.get())
                        d18=Label(donorFrame,text='When are you going to donate this time ?',font=('aria',14))
                        d18.place(x=700,y=380)
                        cal2=DateEntry(donorFrame,width=18,year=2022,month=1,day=1,background='navyblue',fg='white',borderwidth=2)
                        cal2.place(x=700,y=420)
                        d18=Label(donorFrame,text='Where are you going to donate(City) ?',font=('aria',14))
                        d18.place(x=700,y=460)
                        e18=Entry(donorFrame)
                        e18.place(x=700,y=500)
                        e19=Label(donorFrame,text='How much units of Blood will you be donating?',font=('aria',14))
                        e19.place(x=700,y=540)
                        e19=Entry(donorFrame)
                        e19.place(x=700,y=580)
                    else:
                        cal1="None"
                        d18=Label(donorFrame,text='When are you going to donate this time ?',font=('aria',14))
                        d18.place(x=700,y=300)
                        cal2=DateEntry(donorFrame,width=18,year=2022,month=1,day=1,background='navyblue',fg='white',borderwidth=2)
                        cal2.place(x=700,y=340)
                        d18=Label(donorFrame,text='Where are you going to donate(City) ?',font=('aria',14))
                        d18.place(x=700,y=380)
                        e18=Entry(donorFrame)
                        e18.place(x=700,y=420)
                        e19=Label(donorFrame,text='How much units of Blood will you be donating?',font=('aria',14))
                        e19.place(x=700,y=460)
                        e19=Entry(donorFrame)
                        e19.place(x=700,y=500)
                        
                    def submit():
                        try:
                            cursor=conn.cursor()
                            cursor.execute("SELECT * from extradetails where username=?",(username,))
                            output=cursor.fetchall()
                            showdata=""
                            lastdondate=cal1
                            donatedate=cal2.get()
                            donateplace=e18.get()
                            unitblood=e19.get()
                            ub=unitblood
                            cursor.execute("INSERT INTO extradetails VALUES(?,?,?,?,?,?,?)",(username,password,'0','0','0',0,0))
                            cursor.execute("UPDATE extradetails SET lastdondate=?,donatedate=?,donateplace=?,unitdonate=?, points=? where username=?",(lastdondate,donatedate,donateplace,unitblood,unitblood,username,))
                            conn.commit()
                            for i in output:
                                ub=i[5]
                                ub += float(unitblood)
                                cursor.execute("UPDATE extradetails SET unitdonate=? where username=?",(ub,username,))
                                conn.commit()
                            messagebox.showinfo("Status","Submited")
                            cursor.execute("UPDATE extradetails SET points=? where username=?",(ub,username,))
                            conn.commit()
                            Label(donorFrame,text="My Points",font=('Times',18,'bold')).place(x=350,y=50)
                            
                            Label(donorFrame,text=ub,font=('Times',18,'bold')).place(x=550,y=50)
                                
                        except:
                            messagebox.showinfo("Status","Not Submitted")

                    Button(donorFrame,text="Submit",font=('Times',18),command=submit).place(x=850,y=600)
            else:
                messagebox.showinfo("Status","Invalid User")              
                
   except:
       messagebox.showinfo("Status","Invalid User")

lb1=Button(donorFrame,text="Log IN",font=("Times",18,'bold'),command=login,bg='Green',fg='White',width=10).place(x=775,y=115)


#Contact Us Frame
contactFrame=Frame(root)
Label(contactFrame,text="Contact",font=("aria",22,'bold')).place(x=20,y=30)
ph=Image.open("home.jpg")
re=ph.resize((50,50))
im=ImageTk.PhotoImage(re,master=contactFrame)
lab=Label(contactFrame,image=im)
lab.place(x=70,y=100)
lab.image=im
Label(contactFrame,text="Address :",font=(18)).place(x=150,y=100)
Label(contactFrame,text='''PCE Blood Management System
9th floor, Chanderlok Building
35, janpath, New Delhi - 110001,India''',font=(16)).place(x=150,y=140)
ph=Image.open("call.png")
re=ph.resize((50,50))
im=ImageTk.PhotoImage(re,master=contactFrame)
lab=Label(contactFrame,image=im)
lab.place(x=670,y=100)
lab.image=im
Label(contactFrame,text="Call us at :",font=(18)).place(x=750,y=100)
Label(contactFrame,text='''011-43509994

011-23731775''',font=(18)).place(x=750,y=140)
ph=Image.open("email.jpg")
re=ph.resize((50,50))
im=ImageTk.PhotoImage(re,master=contactFrame)
lab=Label(contactFrame,image=im)
lab.place(x=70,y=350)
lab.image=im
Label(contactFrame,text="Write us at :",font=(18)).place(x=150,y=350)
Label(contactFrame,text='''nbmsmohfw123@gmail.com

bloodmgsys123@gmail.com''',font=(18)).place(x=150,y=390)
ph=Image.open("fax.png")
re=ph.resize((50,50))
im=ImageTk.PhotoImage(re,master=contactFrame)
lab=Label(contactFrame,image=im)
lab.place(x=670,y=350)
lab.image=im
Label(contactFrame,text="Fax :",font=(18)).place(x=750,y=350)
Label(contactFrame,text="(856)423-3420",font=(18)).place(x=750,y=390)



#Home Frame
mainFrame=Frame(root)
mainFrame.pack(fill=BOTH,expand=True)

l1=Label(mainFrame,text="PCE BLOOD MANAGEMENT SYSTEM",font=('aria',26,'bold'),fg="Red")
l1.place(x=260,y=50)
image=Image.open("img1.webp")
resized_image= image.resize((300,300))
photo = ImageTk.PhotoImage(resized_image)
image_label = Label(mainFrame,image=photo)
image_label.place(x=50,y=150)
l2=Label(mainFrame,text='"Give the gift of life to others"',font=('aria',18,'bold'),fg='Black')
l2.place(x=30,y=475)
l3=Label(mainFrame,text="Why is it Important to Donate Blood?",font=('aria',18,'bold'))
l3.place(x=580,y=230)
l4=Label(mainFrame,text='''Safe blood saves lives.Blood is the most precious gift that anyone can give to another
person – the gift of life. A decision to donate your blood can save a life, or even several
if your blood is separated into its components – red cells, platelets and plasma – which
can be used individually for patients with specific conditions.''',font=('aria',14))
l4.place(x=420,y=270)
b1=Button(mainFrame,text='LOGIN',font=('aria',14,'bold'),height=2,width=13,fg='RED',bg='White',command=changeToDonor)
b1.place(x=680,y=450)

menubar=Menu(mainFrame)
menubar.add_command(label="Home",command=changeToMain)
menubar.add_command(label="Register",command=changeToReg)
menubar.add_command(label="Donor",command=changeToDonor)
menubar.add_command(label="Search Blood Group",command=changeToSearch)
menubar.add_command(label="Contact us",command=changeToContact)
menubar.add_command(label="About us",command=changeToAbout)

#Registration Form
regFrame=Frame(root)

def sel():
    label.config(text=sel)

d1=Label(regFrame,text='BLOOD DONATION FORM',fg='Red',font=('Oswald',22,'bold'))
d1.place(x=400,y=20)
d2=Label(regFrame,text='Name',font=('aria',14))
d2.place(x=90,y=100)
d3=Label(regFrame,text='Gender',font=('aria',14))
d3.place(x=90,y=140)
d4=Label(regFrame,text='Date Of Birth',font=('aria',14))
d4.place(x=90,y=180)    
d5=Label(regFrame,text='Blood Group',font=('aria',14))
d5.place(x=90,y=220)
d6=Label(regFrame,text='Contact No.',font=('aria',14))
d6.place(x=90,y=260)
d7=Label(regFrame,text='Email',font=('aria',14))
d7.place(x=90,y=300)
d8=Label(regFrame,text='Address',font=('aria',14))
d8.place(x=90,y=340)
d9=Label(regFrame,text='Weight',font=('aria',14))
d9.place(x=90,y=380)
d10=Label(regFrame,text='Pulse',font=('aria',14))
d10.place(x=400,y=380)
d11=Label(regFrame,text='Hb',font=('aria',14))
d11.place(x=90,y=420)
d12=Label(regFrame,text='BP',font=('aria',14))
d12.place(x=400,y=420)
d13=Label(regFrame,text='Temperature',font=('aria',14))
d13.place(x=680,y=380)
d14=Label(regFrame,text='Have you donated previously?',font=('aria',14))
d14.place(x=680,y=420)
d15=Label(regFrame,text='Do you suffer from or have suffered from any of the following diseases?',font=('aria',14))
d15.place(x=90,y=460)
Label(regFrame,text="Select from Below",font=('aria',11)).place(x=90,y=500)    
e1=Entry(regFrame)
e1.place(x=250,y=100)
e2=Entry(regFrame)
e2.place(x=250,y=260)
e3=Entry(regFrame)
e3.place(x=250,y=300)
e4=Entry(regFrame)
e4.place(x=250,y=340)
e5=Entry(regFrame)
e5.place(x=250,y=380)
e6=Entry(regFrame)	
e6.place(x=500,y=380)
e7=Entry(regFrame)
e7.place(x=250,y=420)
e8=Entry(regFrame)
e8.place(x=500,y=420)
e9=Entry(regFrame)
e9.place(x=840,y=380)
e10=Entry(regFrame)
e10.place(x=720,y=465)


c1=Label(regFrame,text="1.Heart Disease",font=(14)).place(x=90,y=530)
c2=Label(regFrame,text="2.Diabetes",font=(14)).place(x=290,y=530)
c3=Label(regFrame,text="3.Sexually Transmitted Disease",font=(14)).place(x=490,y=530)
c4=Label(regFrame,text="6.Lung Disease",font=(14)).place(x=90,y=560)
c5=Label(regFrame,text="7.Allergic Disease",font=(14)).place(x=290,y=560)
c6=Label(regFrame,text="8.Cancer/Malignant Disease",font=(14)).place(x=490,y=560)
c7=Label(regFrame,text="5.Hepatatis B/C",font=(14)).place(x=1000,y=530)
c8=Label(regFrame,text="10.Tuberculosis",font=(14)).place(x=1000,y=560)
c9=Label(regFrame,text="9.Kidney Disease",font=(14)).place(x=760,y=560)
c10=Label(regFrame,text="4.Abnormal Bleeding tendency",font=(14)).place(x=760,y=530)

radio=IntVar()
r1=Radiobutton(regFrame,text="Male",variable=radio,value=1,command=sel,font=('aria',13)).place(x=250,y=140)
r2=Radiobutton(regFrame,text="Female",variable=radio,value=2,command=sel,font=('aria',13)).place(x=330,y=140)
label=Label(regFrame)    
options=['Select Blood Group','A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
clicked=StringVar()
clicked.set("Select Blood Group")
drop=OptionMenu(regFrame,clicked,*options).place(x=250,y=220)

radio1=IntVar()
r3=Radiobutton(regFrame,text="Yes",variable=radio1,value=3,command=sel,font=('aria',14)).place(x=950,y=420)
r4=Radiobutton(regFrame,text="No",variable=radio1,value=4,command=sel,font=('aria',14)).place(x=1050,y=420)
b1=Button(regFrame,text="Register",font=('aria',16,'bold'),bg="red",fg='white',command=reg).place(x=530,y=595) 
label=Label(regFrame)
img=Image.open("img2.jpg").resize((650,300))
w,h = img.size
photo2=ImageTk.PhotoImage(img)
regFrame.photo=photo2
canvas=Canvas(regFrame,width=w,height=h)
canvas.place(x=470,y=70)
canvas.create_image(0,0,anchor='nw',image=photo2)
cal=DateEntry(regFrame,width=18,year=2004,month=1,day=1,background='navyblue',fg='white',borderwidth=2)
cal.place(x=250,y=183)

root.config(menu=menubar)
