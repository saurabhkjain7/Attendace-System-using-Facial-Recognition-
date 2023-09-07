from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import numpy as np
import cv2
import face_recognition
import os
import time



class facedetectWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1580x800+0+0")
        self.root.title("Face Detection")
        self.root.state("zoomed")

        self.var_selected_sub= StringVar()

        top_img = Image.open(r"images\face_detect.jpg")
        top_img = top_img.resize((1580, 800), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(top_img)

        top_img = Label(self.root, image=self.photoimage)
        top_img.Image = top_img
        top_img.place(x=0, y=0, width=1580, height=800)

        button = Button(self.root, text="Detect Face", command=self.face_recog, cursor="hand2",font=("times new roman", 20, "bold"), bg="black", fg="white")
        button.place(x=685, y=725, width=180, height=30)

        # creating combo box
        id_combo = ttk.Combobox(root, textvariable=self.var_selected_sub, font=("times new roman", 20, "bold"),state="readonly", width=18)
        list_id=['select subject','computer networks','theory of computation','compiler design','operating systems']
        id_combo["values"] = tuple(list_id)
        id_combo.current(0)
        id_combo.place(x=530, y=120, width=500, height=40)


    # """""""""""" Face Reognition """""""""""""""""

    def face_recog(self):
        def markAttendance(data_rollno, data_name, data_dep):
            subject=self.var_selected_sub.get()
            date = time.strftime("%d %b %Y ")
            clockin_time = time.strftime("%I:%M:%S %p")
            connect = mysql.connector.connect(host="localhost",user="root",password="Zxcvbnm,",database="face_recognizer",auth_plugin='mysql_native_password')
            my_cursor = connect.cursor()

           #this query is used in order to find whether that student's attendance is already marked or not
            my_cursor.execute("select roll_no,date from attendance where roll_no=%s and date=%s and subject=%s",(data_rollno,date,subject))#bcz we want to mark attendance of a particular student only once in a day
            fetch_data = my_cursor.fetchall()#returns a list of tuples
            # print(fetch_data)

            if len(fetch_data)==0:#bcz we wants to mark attendance only once
                    my_cursor.execute("insert into attendance values(%s,%s,%s,%s,%s,%s)", (
                        data_name,
                        data_rollno,
                        subject,
                        date,
                        data_dep,
                        clockin_time,
                    ))

            connect.commit()
            connect.close()

        #face recognition code starts from here
        path = "data"
        images = []
        classNames = []
        encodeList = []
        myList = os.listdir(path)
        messagebox.showwarning("encoding", "Encoding of images start please don't press anything",parent=self.root)
        for cl in myList:
            curImg = cv2.imread(os.path.join(path, cl))
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])
        # print(classNames)
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)


        messagebox.showinfo("encoding", "Encoding of images complete and  recognition of images started",parent=self.root)
        cap = cv2.VideoCapture(0)

        while True:
            success, img = cap.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)#(0,0) represents we don't define pixel size
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeList, encodeFace)
                faceDis = face_recognition.face_distance(encodeList, encodeFace)
                matchIndex = np.argmin(faceDis)
                # print(matches)

                if matches[matchIndex]:
                    id=classNames[matchIndex]
                    # print(id)
                    connect = mysql.connector.connect(host="localhost",user="root",password="Zxcvbnm,",database="face_recognizer",auth_plugin='mysql_native_password')
                    my_cursor = connect.cursor()

                    my_cursor.execute("select Name from student where Rollno= "+str(id))
                    data_name = my_cursor.fetchone()[0]#we put 0 in subscript bcz it returns tuple as output
                    # print(data_name)

                    my_cursor.execute("select Dep from student where Rollno= " + str(id))
                    data_dep = my_cursor.fetchone()[0]


                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(img,"Name:-"+data_name,(x1-150, y2 +18), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
                    cv2.putText(img,"Roll No.:-"+id, (x1-150, y2+48 ), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
                    cv2.putText(img,"Department:-"+data_dep, (x1-150, y2 + 78), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)


                    markAttendance(id,data_name,data_dep)




            cv2.imshow('webcam', img)
            k = cv2.waitKey(1)
            if k == 27:
                cap.release()
                break



if __name__=="__main__":
    root=Tk()
    obj=facedetectWindow(root)
    root.mainloop()