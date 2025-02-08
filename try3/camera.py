import cv2
import readFace
import os
from time import sleep


os.chdir(r'C:\Users\Bruce\Desktop\programming_workshop2\try3')

COUNTERBREAK = 3

#start camera
cam = cv2.VideoCapture(0)
file_location = "Photo.jpeg"

# status, photo = cam.read()
# cv2.imwrite(file_location, photo)

#save photo and constant replace function if program is running
def imageReplace(browser=None):
    # true is placeholder for later
    variedCounter = 0
    emotionAction = None

    while (True):
        if (browser == None) or browser.isBad():
            status, photo = cam.read()
            cv2.imwrite(file_location, photo)
            sleep(0.5)

            emotionNow = readFace.readF(file_location)

            if emotionNow in ["happy", "nuetral"]:
                variedCounter -= 1
                if variedCounter < 0:
                    variedCounter = 0
                
                if emotionNow == "happy":
                    #happy placeholder action to ui image
                    pass
                else:
                    #neutral placeholder action to ui image
                    pass
                

            elif emotionNow in ["sad", "angry", "disgust"]:
                variedCounter += 1
                
                if emotionNow == "sad":
                    #sad placeholder action to ui image
                    pass
                elif emotionNow == "angry":
                    #angry placeholder action to ui image
                    pass
                else:
                    #disgust placeholder action to ui image
                    pass
                
                if variedCounter >= COUNTERBREAK:
                    #call function to call video action
                    emotionAction = emotionNow
                    break

            else:
                print("Emotion not detected")
        
        
             
           
      


#print(readFace.readF(file_location))