from tkinter import*
from PIL import Image,ImageTk
from student import studentWindow
import os
from face_reco import facedetectWindow
from send_email import emailWindow



class mainWindow:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition System")
        self.root.state("zoomed")

        # background  image
        img1 = Image.open(r"images\background.jpg")
        img1 = img1.resize((1550, 800), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        lab1 = Label(self.root, image=self.photoimage1)#bcz we want to place it on root window
        lab1.Image = img1
        lab1.place(x=0, y=0, width=1550, height=800)

        #title label
        title_lab1 = Label(lab1, text="ATTENDANCE SYSTEM USING FACIAL RECOGNITION", font=("times new roman", 35, "bold"),bg='black',fg="white")
        title_lab1.place(x=0, y=0, width=1530, height=45)

        #student details image
        img2 = Image.open(r"images\student.png")
        img2 = img2.resize((220,220), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        b1 = Button(self.root, image=self.photoimage2,command=self.student_details,cursor='hand2')  # bcz we want to place it on root window
        b1.place(x=180,y=200,width=220,height=220)

        b1_lab = Label(lab1, text="Student Details",font=("times new roman", 20, "italic"), bg='black', fg="white")
        b1_lab.place(x=180, y=420, width=220, height=30)

        # face recognition image
        img3 = Image.open(r"images\face_roco.jpg")
        img3 = img3.resize((220, 220), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        b2 = Button(self.root, command=self.detect_faces,image=self.photoimage3, cursor='hand2')  # bcz we want to place it on root window
        b2.place(x=180, y=500, width=220, height=220)

        b2_lab = Label(lab1, text="Face Recognition", font=("times new roman", 20, "italic"), bg='black', fg="white")
        b2_lab.place(x=180, y=720, width=220, height=30)


       # photos
        img6 = Image.open(r"images\photos.png")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimage6 = ImageTk.PhotoImage(img6)

        b5 = Button(self.root,command=self.show_photos, image=self.photoimage6, cursor='hand2')  # bcz we want to place it on root window
        b5.place(x=1120, y=200, width=220, height=220)

        b4_lab = Label(lab1, text="Photos", font=("times new roman", 20, "italic"), bg='black', fg="white")
        b4_lab.place(x=1120, y=420, width=220, height=30)

        #email
        img7 = Image.open(r"images\email.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimage7 = ImageTk.PhotoImage(img7)

        b6 = Button(self.root,command=self.send_email, image=self.photoimage7, cursor='hand2')  # bcz we want to place it on root window
        b6.place(x=1120, y=500, width=220, height=220)

        b5_lab = Label(lab1, text="Email", font=("times new roman", 20, "italic"), bg='black', fg="white")
        b5_lab.place(x=1120, y=720, width=220, height=30)


    # -----------------------various functions-----------------------------------
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=studentWindow(self.new_window)

    def show_photos(self):
        os.startfile("data")

    def detect_faces(self):
        self.new_window = Toplevel(self.root)
        self.app = facedetectWindow(self.new_window)

    def send_email(self):
        self.new_window = Toplevel(self.root)
        self.app = emailWindow(self.new_window)



if __name__=="__main__":
    root=Tk()
    obj=mainWindow(root)
    root.mainloop()