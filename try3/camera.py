import cv2
import readFace
import os
from time import sleep
import UI
from PyQt6.QtCore import QObject, pyqtSignal


os.chdir(r'C:\Users\Bruce\Desktop\programming_workshop2\try3')
#def setup_signal_connections():
    # Connect the signal to the displayEmotion function
    #emotion_signal.emotion_detected.connect(displayEmotion)

#emotion_signal = EmotionSignal()
#start camera
cam = cv2.VideoCapture(0)
file_location = "Photo.jpeg"

# status, photo = cam.read()
# cv2.imwrite(file_location, photo)

#save photo and constant replace function if program is running
def imageReplace(browser=None):
    print("entered imageReplace")
    # true is placeholder for later
    variedCounter = 0
    emotionAction = None
    COUNTERBREAK= 5
    while (True):
        if (browser == None) or browser.isBad():
            status, photo = cam.read()
            cv2.imwrite(file_location, photo)
            sleep(0.5)

            emotionNow = readFace.readF(file_location)

            if emotionNow in ["happy", "neutral"]:
                variedCounter -= 1
                if variedCounter < 0:
                    variedCounter = 0
                
                if emotionNow == "happy":
                    UI.displayEmotion("😊", "Happy") 
                    pass
                else:
                    UI.displayEmotion("😐", "nuetral") 
                    pass
                

            elif emotionNow in ["sad", "angry", "disgust"]:
                variedCounter += 1
                
                if emotionNow == "sad":
                    UI.displayEmotion("😐", "sad") 
                    pass
                elif emotionNow == "angry":
                    UI.displayEmotion("😡", "Angry")
                    pass
                else:
                    UI.displayEmotion("🤢", "Disgusted")
                    pass
                
                if variedCounter >= COUNTERBREAK:
                    #call function to call video action
                    emotionAction = emotionNow
                    break

            else:
                print("Emotion not detected")

            UI.counterBar(variedCounter, COUNTERBREAK)
        
        
             
           
      


#print(readFace.readF(file_location))