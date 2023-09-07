# Attendace-System-using-Facial-Recognition
<br>
Author - Saurabh Kumar Jain

## Introduction
This project can be used to take students' attendance weekly and then send their weekly attendance to them via their email ID.

## Requirements
The project is 100% written in Python, so need to download a Python IDLE since this project is also integrated with MySQL database so also need to download mysql and mysql workbench.
* Tkinter
* Pillow 
* os
* mysql connector
* numpy
* opencv
* face_recognition
* time
* cmake
* dlib

## Description of files
* main.py: This python file contains code of the graphical user interface of the main window of the project, which is used to go to other parts of projects.
* student.py: This python file contains code that can be used to store details, delete details, update details, reset details, take photos, and update photos of students in MySQL database.
* face_reco.py: This python file contains code that can able to recognize students based on student details which is already stored in the database and then take attendance of student day-wise and then stores it into another database.
* send_email.py: This python file contains code that helps us to email weekly attendance to students.
* upload.py: This python file contains code that helps us to browse photos of students in order to upload it.


