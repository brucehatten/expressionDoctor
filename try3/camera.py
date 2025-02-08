import cv2
import readFace
import os


os.chdir(r'C:\Users\Bruce\Desktop\programming_workshop2\try3')


#start camera
cam = cv2.VideoCapture(0)
file_location = "Photo.jpeg"

status, photo = cam.read()
cv2.imwrite(file_location, photo)

#save photo and constant replace function if program is running
def imageReplace():
    # true is placeholder for later
    while (True):
        status, photo = cam.read()
        cv2.imwrite(file_location, photo)

        emotionNow = readFace(file_location)
        if emotionNow == "happy":
            pass
            #happy placeholder action
        elif emotionNow == "sad":
            pass
            #sad placeholder action
        elif emotionNow == "angry":
            pass
            #angry placeholder action
        else:
            print("Error Found")


print(readFace.readF(file_location))