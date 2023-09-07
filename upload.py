from tkinter import*
from tkinter import filedialog
import os
from PIL import Image,ImageTk
import cv2
from tkinter import messagebox


class uploadPhoto:
    def __init__(self,root):
        self.root=root
        self.root.geometry("350x300+0+0")
        self.root.title("Uploading the Photo")


        lbl = Label(root,font=("times new roman", 35, "bold"), bg="white",fg="black")
        lbl.place(x=0, y=0, width=350, height=250)

        btn1 = Button(root, text="Browse Photo",command=lambda:self.show_image(lbl),font=("times new roman", 10, "bold"), fg="black", bg="white")
        btn1.place(x=50,y=260,width=100)

        btn2 = Button(root, text="Upload Photo",command=self.upload_image, font=("times new roman", 10, "bold"), fg="black", bg="white")
        btn2.place(x=200, y=260, width=100)


    def show_image(self,lbl):
        global path
        path=filedialog.askopenfilename(initialdir=os.getcwd(),title="select Image File",filetypes=(("JPG FILE","*.jpg"),("PNG FILE","*.png"),("ALL FILES","*.*")),parent=self.root)
        img=Image.open(path)
        img.thumbnail((350,250))#to make imagae fit to our window
        img=ImageTk.PhotoImage(img)
        lbl.configure(image=img)
        lbl.image=img

    def upload_image(self):
        messagebox.showinfo("uploading the photo","photo uploading got started",parent=self.root)
        img=cv2.imread(path)
        file_name_path = "data/" + "new" + ".jpg"
        cv2.imwrite(file_name_path,img)
        messagebox.showinfo("uploading the photo", "photo uploading got completed", parent=self.root)




if __name__=="__main__":
    path = ""
    root=Tk()
    obj=uploadPhoto(root)
    root.mainloop()