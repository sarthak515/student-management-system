from tkinter import *
from tkinter import ttk
import pymysql
from  tkinter import messagebox
root=Tk()
root.title("STUDENT MANAGEMENT SYSTEM")
root.geometry("1350x700+0+0")
def add_students():
    if Roll_No_var.get()=="" or name_var.get()=="":
        messagebox.showerror("Error","all fields are required")
    else:
        con = pymysql.connect(host="localhost", user="root", password="Sarthak@123", database="stm")
        cur = con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (
        Roll_No_var.get(), name_var.get(), email_var.get(), gender_var.get(), contact_var.get(), dob_var.get(),
        txt_address.get('1.0', END)))
        con.commit()
        fetch_data()
        clear()
        con.close
        messagebox.showinfo("success","record has been inserted")

def fetch_data():
    con=pymysql.connect(host="localhost",user="root",password="Sarthak@123",database="stm")
    cur=con.cursor()
    cur.execute("select * from students")
    rows=cur.fetchall()
    if len(rows)!=0:
        Student_table.delete(*Student_table.get_children())
        for row in rows:
             Student_table.insert('',END,values=row)
        con.commit()
    con.close()
def clear():
    Roll_No_var.set("")
    name_var.set("")
    email_var.set("")
    gender_var.set("")
    contact_var.set("")
    dob_var.set("")
    txt_address.delete("1.0",END)

def get_cursor(ev):
    cursor_row=Student_table.focus()
    contents=Student_table.item(cursor_row)
    row=contents['values']
    Roll_No_var.set(row[0])
    name_var.set(row[1])
    email_var.set(row[2])
    gender_var.set(row[3])
    contact_var.set(row[4])
    dob_var.set(row[5])
    txt_address.delete("1.0", END)
    txt_address.insert(END,row[6])

def update():
    con = pymysql.connect(host="localhost", user="root", password="Sarthak@123", database="stm")
    cur = con.cursor()
    cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where Roll_No=%s",
    (name_var.get(), email_var.get(), gender_var.get(), contact_var.get(), dob_var.get(),
    txt_address.get('1.0', END),Roll_No_var.get()))
    con.commit()
    fetch_data()
    clear()
    con.close

def delete():
    con=pymysql.connect(host="localhost",user="root",password="Sarthak@123",database="stm")
    cur=con.cursor()
    cur.execute("delete from students where Roll_no=%s",Roll_No_var.get())
    con.commit()
    con.close()
    fetch_data()
    clear()

def search_data():
    con=pymysql.connect(host="localhost",user="root",password="Sarthak@123",database="stm")
    cur=con.cursor()
    cur.execute("select * from students where"+str(search_by.get())+" LIKE '%"+str(search_txt.get())+"%'")
    rows=cur.fetchall()
    if len(rows)!=0:
        Student_table.delete(*Student_table.get_children())
        for row in rows:
             Student_table.insert('',END,values=row)
        con.commit()
    con.close()
#setting title
title=Label(root,text="Student management System",bd=10,relief=GROOVE,font="lucida 40 bold",bg="yellow",fg="red")
title.pack(side=TOP,fill=X)

        #all variables
Roll_No_var=StringVar()
name_var=StringVar()
email_var=StringVar()
gender_var=StringVar()
contact_var=StringVar()
dob_var=StringVar()
search_by=StringVar()
search_txt=StringVar()

#setting frame 1
manage_Frame=Frame(root,bd=4,relief=RIDGE,bg="crimson")
manage_Frame.place(x=20,y=100,width=450,height=600)
        # title in frame1
m_title=Label(manage_Frame,text="Manage Students",bg="crimson" ,fg="white", font=("times new roman",30, "bold"))
m_title.grid(row=0,columnspan=2,pady=20)
        #adding rollno
lbl_roll=Label(manage_Frame,text="Roll-No",bg="crimson" ,fg="white",font=("times new roman",20, "bold"))
lbl_roll.grid(row=1,column=0,padx=20,pady=10,sticky="w")
        #adding roll no entry
txt_roll=Entry(manage_Frame,textvariable=Roll_No_var,font=("times new roman",15, "bold"),bd=5,relief=GROOVE)
txt_roll.grid(row=1,column=1,padx=20,pady=10,sticky="w")
        #adding name
lbl_name=Label(manage_Frame,text="Name",bg="crimson" ,fg="white",font=("times new roman",20,"bold"))
lbl_name.grid(row=2,column=0,padx=20,pady=10,sticky="w")
        #adding name entry
txt_name=Entry(manage_Frame,textvariable=name_var,font=("times new roman",15, "bold"),bd=5,relief=GROOVE)
txt_name.grid(row=2,column=1,padx=20,pady=10,sticky="w")
        #adding email
lbl_email=Label(manage_Frame,text="Email",bg="crimson" ,fg="white",font=("times new roman",20,"bold"))
lbl_email.grid(row=3,column=0,padx=20,pady=10,sticky="w")
       # adding email entry
lbl_email=Entry(manage_Frame,textvariable=email_var,font=("times new roman",15, "bold"),bd=5,relief=GROOVE)
lbl_email.grid(row=3,column=1,padx=20,pady=10,sticky="w")

        #adding gender
lbl_gender=Label(manage_Frame,text="Gender",bg="crimson" ,fg="white",font=("times new roman",20,"bold"))
lbl_gender.grid(row=4,column=0,padx=20,pady=10,sticky="w")
       # adding gender combobox
combo_gender=ttk.Combobox(manage_Frame,textvariable=gender_var,font=("times new roman",13,"bold"),state='readonly')
combo_gender['values']=("male","female","other")
combo_gender.grid(row=4,column=1,padx=20,pady=10)

        #adding contact
lbl_contact=Label(manage_Frame,text="Contact No",bg="crimson" ,fg="white",font=("times new roman",20,"bold"))
lbl_contact.grid(row=5,column=0,padx=20,pady=10,sticky="w")
       # adding contact entry
lbl_contact=Entry(manage_Frame,textvariable=contact_var,font=("times new roman",15, "bold"),bd=5,relief=GROOVE)
lbl_contact.grid(row=5,column=1,padx=20,pady=10,sticky="w")
        #adding dob
lbl_dob=Label(manage_Frame,text=" D.O.B",bg="crimson" ,fg="white",font=("times new roman",20,"bold"))
lbl_dob.grid(row=6,column=0,padx=20,pady=10,sticky="w")
       # adding dob entry
lbl_dob=Entry(manage_Frame,textvariable=dob_var,font=("times new roman",15, "bold"),bd=5,relief=GROOVE)
lbl_dob.grid(row=6,column=1,padx=20,pady=10,sticky="w")

        #adding addresss
lbl_address=Label(manage_Frame,text="Address",bg="crimson" ,fg="white",font=("times new roman",20,"bold"))
lbl_address.grid(row=7,column=0,padx=20,pady=10,sticky="w")

txt_address=Text(manage_Frame,width=30,height=4,font=("",10))
txt_address.grid(row=7,column=1,padx=10,pady=20,sticky="w")

#button frame
btn_frame=Frame(manage_Frame,bd=4,relief=RIDGE,bg="crimson")
btn_frame.place(x=15,y=530,width=420)

#adding buttons
addbtn=Button(btn_frame,text="Add",width=10,command=add_students).grid(row=0,column=0,padx=10,pady=10)
updatebtn=Button(btn_frame,text="Update",width=10,command=update).grid(row=0,column=1,padx=10,pady=10)
deletebtn=Button(btn_frame,text="Delete",width=10,command=delete).grid(row=0,column=2,padx=10,pady=10)
clearbtn=Button(btn_frame,text="Clear",width=10,command=clear).grid(row=0,column=3,padx=10,pady=10)



#setting frame 2
Detail_Frame=Frame(root,bd=4,relief=RIDGE,bg="crimson")
Detail_Frame.place(x=500,y=100,width=1000,height=600)
        #adding search label
lbl_search=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
lbl_search.grid(row=0,column=0,padx=20,pady=10,sticky="w")
        #combo search box
combo_search=ttk.Combobox(Detail_Frame,textvariable=search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
combo_search['values']=("roll","name","contact")
combo_search.grid(row=0,column=1,padx=20,pady=10)
        #addin entry for search
txt_search=Entry(Detail_Frame,textvariable=search_txt,width=15,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
txt_search.grid(row=0,column=2,padx=10,pady=20,sticky="w")

        #buttons for search and show
searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=search_data).grid(row=0,column=3,padx=10,pady=10)
showallbtn=Button(Detail_Frame,text="show all",width=10,pady=5,command=fetch_data).grid(row=0,column=4,padx=10,pady=10)

        #table frame
table_frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
table_frame.place(x=10,y=70,width=800,height=500)

scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
scroll_y=Scrollbar(table_frame,orient=VERTICAL)

Student_table=ttk.Treeview(table_frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=Student_table.xview)
scroll_y.config(command=Student_table.yview)
Student_table.heading("roll",text="Roll no")
Student_table.heading("name",text="name")
Student_table.heading("email",text="Email")
Student_table.heading("gender",text="gender")
Student_table.heading("contact",text="contact")
Student_table.heading("dob",text="DOB")
Student_table.heading("address",text="address")
Student_table['show']='headings'
        #setting width
Student_table.column("roll",width=100)
Student_table.column("name",width=100)
Student_table.column("email",width=100)
Student_table.column("gender",width=100)
Student_table.column("contact",width=100)
Student_table.column("dob",width=100)
Student_table.column("address",width=150)

Student_table.pack(fill=BOTH,expand=1)
Student_table.bind("<ButtonRelease-1>",get_cursor)
fetch_data()



root.mainloop()
