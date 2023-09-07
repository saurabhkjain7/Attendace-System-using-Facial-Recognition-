from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import time
import os
from upload import uploadPhoto


class studentWindow:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Student Details")
        self.root.state("zoomed")
        
        
        # """""""""""""" Variables """"""""""""""""""
        
        self.var_dep=StringVar()
        self.var_semester=StringVar()
        self.var_rollno = StringVar()
        self.var_studentname=StringVar()
        self.var_div=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()


        #Fist image
        img=Image.open(r"images\logo.jpg")
        img=img.resize((200,130),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)   
        
        labl=Label(self.root,image=self.photoimage)
        labl.Image=img
        labl.place(x=0,y=0,width=200,height=130)
        #second image
        img2=Image.open(r"images\clg.jpg")
        img2=img2.resize((1350,130),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img2)

        labl1=Label(self.root,image=self.photoimage1)
        labl1.Image=img2
        labl1.place(x=200,y=0,width=1350,height=130)
        #bg image
        img3=Image.open(r"images\background.jpg")
        img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img3)

        bg_image=Label(self.root,image=self.photoimage2)
        bg_image.Image=img
        bg_image.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_image,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_image,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame

        left_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE,font=("times new roman",12,"bold"),text="Student Details")
        left_frame.place(x=10,y=10,width=730,height=580)
        left_img=Image.open(r"images\std.jpg")
        left_img.resize((700,130),Image.ANTIALIAS)
        self.photoimage_left=ImageTk.PhotoImage(left_img)

        f_image=Label(left_frame,image=self.photoimage_left)
        f_image.Image=left_img
        f_image.place(x=5,y=0,width=720,height=130)

        #current course frame
        current_course=LabelFrame(left_frame,bd=2,bg="white", relief=RIDGE,font=("times new roman",12,"bold"),text="Current Course Information")
        current_course.place(x=5,y=165,width=720,height=80)
        #Department
        dep_lbl=Label(current_course,text="Department",bg="white",font=("times new roman",12,"bold"))
        dep_lbl.grid(row=0,column=0,padx=5)
        dep_combo=ttk.Combobox(current_course,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","computer science","IT","Civil","Mechanical","Electrical","Mining")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Semester combobox
        sem_lbl=Label(current_course,text="Semester",bg="white",font=("times new roman",12,"bold"))
        sem_lbl.grid(row=0,column=2,padx=5)
        sem_combo=ttk.Combobox(current_course,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        sem_combo["values"]=("Select Semester","First","Second","Third","Fourth","Fith","Six","Seven","Eight")
        sem_combo.current(0)
        sem_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Class student information
        class_std=LabelFrame(left_frame,bd=2,bg="white", relief=RIDGE,font=("times new roman",12,"bold"),text="Class Studnet Information")
        class_std.place(x=5,y=290,width=720,height=265)


        # roll number
        stdID_lbl = Label(class_std, text="Roll Number", bg="white", font=("times new roman", 13, "bold"))
        stdID_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        stdID_entry = ttk.Entry(class_std, textvariable=self.var_rollno, width=20, font=("times new roman", 12, "bold"))
        stdID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # StudentName
        stdID_lbl = Label(class_std, text="Student Name", bg="white", font=("times new roman", 13, "bold"))
        stdID_lbl.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        stdID_entry = ttk.Entry(class_std, textvariable=self.var_studentname, width=20,font=("times new roman", 12, "bold"))
        stdID_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # classdivision
        div_lbl = Label(class_std, text="Class Division", bg="white", font=("times new roman", 13, "bold"))
        div_lbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        div_combo = ttk.Combobox(class_std, textvariable=self.var_div, font=("times new roman", 12, "bold"),state="readonly", width=18)
        div_combo["values"] = ("Select", "A1", "A2","A3","A4","B1","B2","C1","C2")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Address
        stdID_lbl = Label(class_std, text="Address", bg="white", font=("times new roman", 13, "bold"))
        stdID_lbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        stdID_entry = ttk.Entry(class_std, width=20, textvariable=self.var_address,font=("times new roman", 12, "bold"))
        stdID_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)



        #Gender
        gender_lbl = Label(class_std, text="Gender", bg="white", font=("times new roman", 13, "bold"))
        gender_lbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        gender_combo = ttk.Combobox(class_std, textvariable=self.var_gender, font=("times new roman", 12, "bold"),state="readonly", width=18)
        gender_combo["values"] = ("Select ", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        #DOB
        stdID_lbl=Label(class_std,text="DOB",bg="white",font=("times new roman",13,"bold"))
        stdID_lbl.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        stdID_entry=ttk.Entry(class_std,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        stdID_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        stdID_lbl=Label(class_std,text="Email",bg="white",font=("times new roman",13,"bold"))
        stdID_lbl.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        stdID_entry=ttk.Entry(class_std,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        stdID_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone number
        stdID_lbl=Label(class_std,text="Phone Number",bg="white",font=("times new roman",13,"bold"))
        stdID_lbl.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        stdID_entry=ttk.Entry(class_std,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        stdID_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)




        #Button Frame
        button_frame=Frame(class_std,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=193,width=714,height=24)

        #Save_Button
        save_btn=Button(button_frame,text="Save",command=self.add_data,font=("times new roman",10,"bold"),fg="white",bg="blue",width=24)
        save_btn.grid(row=0,column=0)

        #Update_Button
        update_btn=Button(button_frame,text="Update",command=self.update_data,font=("times new roman",10,"bold"),fg="white",bg="blue",width=24)
        update_btn.grid(row=0,column=1)

        #reset_Button
        reset_btn=Button(button_frame,text="Reset",command=self.reset_data,font=("times new roman",10,"bold"),fg="white",bg="blue",width=24)
        reset_btn.grid(row=0,column=2)

        #delete_Button
        dlt_btn=Button(button_frame,text="Delete",command=self.delete_data,font=("times new roman",10,"bold"),fg="white",bg="blue",width=24)
        dlt_btn.grid(row=0,column=3)

        #photo Frame
        photo_frame=Frame(class_std,bd=2,relief=RIDGE,bg="white")
        photo_frame.place(x=0,y=217,width=714,height=24)

        #Take photo_ Button
        photo_btn=Button(photo_frame,text="Take Photo Sample",command=self.take_photo,font=("times new roman",10,"bold"),fg="white",bg="blue",width=33)
        photo_btn.grid(row=0,column=0)

        #Upload _photo Button
        nphoto_btn=Button(photo_frame,text="Upload Photo Sample",command=self.upload_photo,font=("times new roman",10,"bold"),fg="white",bg="blue",width=33)
        nphoto_btn.grid(row=0,column=1)

        # save photo Button
        sphoto_btn = Button(photo_frame, text="Save uploaded photo",command=self.save_photo,font=("times new roman", 10, "bold"), fg="white", bg="blue", width=33)
        sphoto_btn.grid(row=0, column=2)

        #right label frame

        right_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE,font=("times new roman",12,"bold"),text="Student Details")
        right_frame.place(x=760,y=10,width=720,height=580)
        right_img=Image.open(r"images\std.jpg")
        right_img.resize((710,130),Image.ANTIALIAS)
        self.photoimage_right=ImageTk.PhotoImage(right_img)

        R_image=Label(right_frame,image=self.photoimage_right)
        R_image.Image=right_img
        R_image.place(x=5,y=0,width=710,height=130)


        # /////////////Table Frame////////////

        table_Frame=Frame(right_frame,bd=2,bg="white", relief=RIDGE)
        table_Frame.place(x=5,y=150,width=705,height=400)

        #////////scroll bar //////////
        scroll_x=ttk.Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_Frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_Frame,column=("dep","semester","rollno","studentname","div","gender","dob","email","phone","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("rollno",text="RollNumber")
        self.student_table.heading("studentname",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=150)
        self.student_table.column("semester",width=100)
        self.student_table.column("rollno",width=150)
        self.student_table.column("studentname",width=200)
        self.student_table.column("div", width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=200)
        self.student_table.column("phone",width=200)
        self.student_table.column("address",width=300)



        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)#when we click on data of table it shuld show on class student information
        self.fetch_data()


    # """""""""""""""" Adding data into database """"""""""""""""""""
    def add_data(self):
        if self.var_dep.get() =="Select Department"  or self.var_semester.get() =="" or self.var_rollno.get() =="" or self.var_studentname.get() =="" or self.var_div.get() =="Select" or self.var_gender.get() =="Select" or self.var_dob.get() =="" or self.var_email.get() =="" or self.var_phone.get() =="" or self.var_address.get() =="":
            messagebox.showerror('Error','All Fields are required',parent=self.root)
        else:
                connect=mysql.connector.connect(host="localhost",user="root",password="Zxcvbnm,",database="face_recognizer",auth_plugin='mysql_native_password')#takes 4 parameters
                my_cursor=connect.cursor()#cursor is used to execute sql queries
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                      self.var_dep.get(),
                                                      self.var_semester.get(),
                                                      self.var_rollno.get(),
                                                      self.var_studentname.get(),
                                                      self.var_div.get(),
                                                      self.var_gender.get(),
                                                      self.var_dob.get(),
                                                      self.var_email.get(),
                                                      self.var_phone.get(),
                                                      self.var_address.get(),

                       ))
                connect.commit()#use to update data
                self.fetch_data()
                connect.close()#use to close connection with database
                messagebox.showinfo("sucess","stundent details has been added successfully",parent=self.root)#bcz we want to open message box on parent


    # """""""""""""""" Fetch Data """"""""""""""""""""
    def fetch_data(self):
        connect=mysql.connector.connect(host="localhost",user="root",password="Zxcvbnm,",database="face_recognizer",auth_plugin='mysql_native_password')#takes 4 arguments
        my_cursor=connect.cursor()#use to run sql queries
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()#varibale that is used to fetch all data

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())#this is used to first delete all data of our table in gui
            for i in data:
                self.student_table.insert("",END,values=i)#used to insert in table of our gui
            connect.commit()
        connect.close()


    # """""""""""""Get Cursor """""""""""

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()#used for focussing the cursor
        content = self.student_table.item(cursor_focus)
        data = content["values"]#bcz in content we have heading as well as values related to those headings
        self.var_dep.set(data[0]),
        self.var_semester.set(data[1]),
        self.var_rollno.set(data[2]),
        self.var_studentname.set(data[3]),
        self.var_div.set(data[4]),
        self.var_gender.set(data[5]),
        self.var_dob.set(data[6]),
        self.var_email.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_address.set(data[9]),


    # """""""""""""""""""Update data """"""""""

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_semester.get() == "" or self.var_rollno.get() == "" or self.var_studentname.get() == "" or self.var_div.get() == "Select" or self.var_gender.get() == "Select" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
                Update = messagebox.askyesno("update", "Do you want update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost",user="root",password="Zxcvbnm,",database="face_recognizer",auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set `Dep`=%s,`Semester`=%s,`Rollno`=%s,`Name`=%s,`Division`=%s,`Gender`=%s,`Dob`=%s,`Email`=%s,`Phone`=%s,`Address`=%s where Rollno=%s",
                        (
                            self.var_dep.get(),
                            self.var_semester.get(),
                            self.var_rollno.get(),
                            self.var_studentname.get(),
                            self.var_div.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_rollno.get()

                        ))

                else:
                    if not Update:
                        return
                messagebox.showinfo("sucess", "student details sucessfully update", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

    # """""""""""""""""""Delete data """"""""""
    def delete_data(self):
        if self.var_rollno.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)

        else:
                delete = messagebox.askyesno("Student delete page", "Do you want to delete this student details", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost",user="root",password="Zxcvbnm,",database="face_recognizer",auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor()
                    sql = "delete from student where Rollno = %s"
                    my_cursor.execute(sql, (self.var_rollno.get(),))
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete", "student details sucessfully deleted", parent=self.root)

        # """""""""""""""""""Reset data """""""""""""""""""""""

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_semester.set("Select Semester")
        self.var_rollno.set("")
        self.var_studentname.set("")
        self.var_div.set("Select")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")



    #"""""""""""""Capturing photo via webcam""""""""""
    def take_photo(self):
        if(self.var_dep.get() == "Select Department" or self.var_semester.get() == "" or self.var_rollno.get() == "" or self.var_studentname.get() == "" or self.var_div.get() == "Select" or self.var_gender.get() == "Select" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == ""):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            global id
            id=self.var_rollno.get()
            cap = cv2.VideoCapture(0)
            count=5
            while True:
                ret, my_frame = cap.read()
                cv2.putText(my_frame, str(count), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 2)
                count = count - 1
                cv2.imshow("Capturing the photo",my_frame)
                cv2.waitKey(1)
                time.sleep(1)
                if count==-1:
                    break
            ret,my_frame=cap.read()
            file_name_path = "data/"+ str(id) + ".jpg"
            cv2.imwrite(file_name_path, my_frame)
            cv2.imshow("Capturing the photo", my_frame)
            k=cv2.waitKey(1)
            if(k==27):
                cap.release()

    def upload_photo(self):
        self.new_window = Toplevel(self.root)
        self.app = uploadPhoto(self.new_window)

    def save_photo(self):
        id=self.var_rollno.get()
        img = cv2.imread("data/new.jpg")
        file_name_path = "data/" + str(id) + ".jpg"
        cv2.imwrite(file_name_path, img)
        #deleting the previous file
        file = 'new.jpg'
        location = "data"
        path=os.path.join(location, file)
        os.remove(path)



if __name__=="__main__":
    id=""
    root=Tk()
    obj=studentWindow(root)
    root.mainloop()       
        






