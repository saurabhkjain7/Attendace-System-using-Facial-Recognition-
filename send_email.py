from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import smtplib as s


class emailWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1580x800+0+0")
        self.root.title("sending mail")
        self.root.state("zoomed")

        self.var_selected_id= StringVar()
        self.var_selected_sub= StringVar()
        self.var_selected_sub1=StringVar()

        # background  image
        img1 = Image.open(r"images\email_1.jpg")
        img1 = img1.resize((1550, 800), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        bg1 = Label(self.root, image=self.photoimage1)  # bcz we want to place it on root window
        bg1.Image = img1
        bg1.place(x=0, y=0, width=1550, height=800)

        #logo
        img2 = Image.open(r"images\email_2.png")
        img2 = img2.resize((250,150), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        bg2 = Label(self.root, image=self.photoimage2)  # bcz we want to place it on root window
        bg2.Image = img2
        bg2.place(x=650, y=25, width=250, height=150)


        #send to specific code

        #left label
        lab_1 = Label(self.root, text="Send To Specific Student Using Roll Number", font=("times new roman", 20, "bold"), bg='pink', fg="black")
        lab_1.place(x=70, y=240, width=600, height=40)


        #fetching the data for our dropdown box
        connect = mysql.connector.connect(host="localhost",user="root",password="Zxcvbnm,",database="face_recognizer",auth_plugin='mysql_native_password')  # takes 4 arguments
        my_cursor = connect.cursor()  # use to run sql queries
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()  # varibale that is used to fetch all data
        i = 0
        list_id=[]
        list_id.append("select student Roll Number")
        while i<len(data):
            list_id.append(data[i][2])
            i=i+1

        #creating combo box for student id
        id_combo = ttk.Combobox(root, textvariable=self.var_selected_id, font=("times new roman", 20, "bold"),state="readonly", width=18)
        id_combo["values"] =tuple(list_id)
        id_combo.current(0)
        id_combo.place(x=70,y=400,width=600,height=40)
        connect.commit()
        connect.close()

        #creating combo box for subject
        id_combo1 = ttk.Combobox(root, textvariable=self.var_selected_sub, font=("times new roman", 20, "bold"),state="readonly", width=18)
        list_id1 = ['select subject', 'computer networks', 'theory of computation', 'compiler design','operating systems']
        id_combo1["values"] = tuple(list_id1)
        id_combo1.current(0)
        id_combo1.place(x=70, y=560, width=600, height=40)


        button = Button(self.root, text="Send Specific", command=self.sendtospecific, cursor="hand2",font=("times new roman", 20, "bold"), relief='ridge', borderwidth=5, bg="yellow", fg="black")
        button.place(x=230, y=720, width=280, height=40)

        # send to all code

        # left label
        lab_2 = Label(self.root, text="Send To All Students",font=("times new roman", 20, "bold"), bg='pink', fg="black")
        lab_2.place(x=870, y=240, width=600, height=40)


        # creating combo box for subject
        id_combo2 = ttk.Combobox(root, textvariable=self.var_selected_sub1, font=("times new roman", 20, "bold"),state="readonly", width=18)
        list_id2 = ['select subject', 'computer networks', 'theory of computation', 'compiler design','operating systems']
        id_combo2["values"] = tuple(list_id2)
        id_combo2.current(0)
        id_combo2.place(x=870, y=400, width=600, height=40)

        # bottom button
        button = Button(self.root, text="Send All", command=self.sendmailfunc, cursor="hand2",font=("times new roman", 20, "bold"), relief="ridge", borderwidth=5, bg="yellow", fg="black")
        button.place(x=1040, y=560, width=280, height=40)

    def sendtospecific(self):
        id=self.var_selected_id.get()
        subject=self.var_selected_sub.get()

        connect = mysql.connector.connect(host="localhost", user="root", password="Zxcvbnm,",database="face_recognizer",auth_plugin='mysql_native_password')  # takes 4 arguments
        my_cursor = connect.cursor()
        my_cursor.execute("select roll_no,count(*) from attendance group by roll_no,subject having roll_no=%s and subject=%s",(id,subject))
        data = my_cursor.fetchone()
        connect.commit()
        connect.close()

        if data is not None:
            attenforid=round((data[1]/6)*100,2)#collects attendance for that id
        else:
            attenforid=0

        connect = mysql.connector.connect(host="localhost", user="root", password="Zxcvbnm,",database="face_recognizer",auth_plugin='mysql_native_password')  # takes 4 arguments
        my_cursor = connect.cursor()
        my_cursor.execute("select Name,Email from student where Rollno="+id)
        data = my_cursor.fetchone()
        connect.commit()
        connect.close()

        nameforid=data[0]#collects name for that id
        emailforid=data[1]#collects email for that id


        messagebox.showinfo("Started", "sending email to " + nameforid + " got strated",parent=self.root)
        #sendign mail procedure
        ob = s.SMTP("smtp.gmail.com", 587)
        ob.starttls()
        ob.login("jainsaurabh0124@gmail.com", "Zxcvbnm,1234")

        subject_email = "your weekly attendance report from MBM engineering college"
        body = "hello " + nameforid + " your weekly attendance percentage in "+subject+" is " + str(attenforid) + "% "
        message = "Subject:{}\n\n{}".format(subject_email, body)

        ob.sendmail("jainsaurabh0124",emailforid, message)
        ob.quit()
        messagebox.showinfo("Completed", "sending email to "+nameforid+" got completed",parent=self.root)


    def sendmailfunc(self):
        subject = self.var_selected_sub1.get()
        connect = mysql.connector.connect(host="localhost", user="root", password="Zxcvbnm,",database="face_recognizer",auth_plugin='mysql_native_password')  # takes 4 arguments
        my_cursor = connect.cursor()  # use to run sql queries
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()  # varibale that is used to fetch all data
        i=0
        st_details=dict()
        st_id=[]
        while i<len(data):
            st_id.append(data[i][2])
            st_details[data[i][2]]=[data[i][3],data[i][7]]
            i=i+1
        connect.commit()
        connect.close()

        print(st_id)
        print(st_details)
        atten_p=dict()#in this key will be roll_no and value will be percentage that roll_no appears in clase
        connect = mysql.connector.connect(host="localhost", user="root", password="Zxcvbnm,",database="face_recognizer",auth_plugin='mysql_native_password')  # takes 4 arguments
        my_cursor = connect.cursor()# use to run sql queries
        my_cursor.execute("select roll_no,count(*) from attendance group by roll_no having subject="+subject)
        data = my_cursor.fetchall()
        print(data)

        i=0
        while i<len(data):
            x=((data[i][1])/6)*100
            x=round(x,2)
            atten_p[data[i][0]]=x
            i=i+1
        connect.commit()
        connect.close()


        messagebox.showinfo("Started", "sending email to all got strated",parent=self.root)
        #sending email to the students
        ob = s.SMTP("smtp.gmail.com", 587)
        ob.starttls()
        ob.login("jainsaurabh0124@gmail.com", "Zxcvbnm,1234")

        for id in st_id:
            subject_email = "your weekly attendance report from MBM engineering college"
            if id in atten_p.keys():
                body = "hello "+st_details[id][0]+" your weekly attendance percentage in "+ subject +" is " +str(atten_p[id])+"% "
            else:
                body = "hello " + st_details[id][0] + " your weekly attendance percentage in "+ subject +" is 0 %"


            message = "Subject:{}\n\n{}".format(subject_email, body)
            ob.sendmail("jainsaurabh0124", st_details[id][1], message)

        ob.quit()
        messagebox.showinfo("Completed", "sending email to all the students got completed",parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=emailWindow(root)
    root.mainloop()