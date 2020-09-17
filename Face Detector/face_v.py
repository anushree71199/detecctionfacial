#Code for Python_Face_Detection_Video
#importing the libraries
#Code block 1
pip install opencv-python
import numpy as np
import cv2
#Code block 2
#loading the haarcascade file make sure to keep the haarcascade file in the same directory
face_cascade= cv2.CascadeClassifier('haarcascade-frontalface_default.xml')
#to capture the video on the web cam
cap = cv2.VideoCapture(0)
#looping statement to let the camera role and detect the face until the user presses key 27 to exit the camera mode and shut the camera down
#Code block 3
while True:
    ret,img= cap.read()  #To read the captured video
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)       
    face_cascade.load('haarcascade_frontalface_default.xml')  #loading the haarcascade file to detect the fronatal face XML again and again
    faces = face_cascade.detectMultiScale(gray, 1.1,5)     
    #looping statement to read the face in a rectangle form where x,y,x+w,y+h is top straight line, lower right, upper right, lower left respectively to make a rectangle surrounding the face   
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255, 0, 0), 2)
        roi_gray= gray[y:y+h, x:x+w]
        roi_color= img[y:y+h, x:x+w]
    cv2.imshow('img',img)  #to show the detected face on the screen
    k=cv2.waitKey(30)& 0xff
    if(k==27):   #to break the loop and turn off the detection
        break
    
cap.release()
