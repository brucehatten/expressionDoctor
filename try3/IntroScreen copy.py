from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QProgressBar
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QTimer
import threading


sadEmoji= "😭"
fearEmoji= "😱"
angryEmoji= "😡"
disgustEmoji= "🤢"
neutralEmoji= "😐"
happyEmoji= "😊"

emojiArray = [sadEmoji, fearEmoji, angryEmoji, disgustEmoji, neutralEmoji, happyEmoji]
def runFile():
    import mainTest
    mainTest.main()



def curentEmotionWindow():
    curentEmotionWindow = QWidget()
    curentEmotionWindow.setWindowTitle(None)
    curentEmotionWindow.setGeometry(0, 0, 300, 200)  # Top-left corner
    curentEmotionWindow.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)  # Stay on top
    curentEmotionWindow.setStyleSheet("background-color: #f4f4f9;")  # Light background color
    curentEmotionWindow.show()

def on_button_click():
    label.setText("LOADING... :)")
    button.setDisabled(True)  
    progressBar.setValue(0)    
    
    # Start the timer to simulate loading
    timer.start(50)  # Timer 

def update_progress():
    value = progressBar.value()
    if value < 100:
        progressBar.setValue(value + 1)  # Increment progress by 1
        if value < 16:
            emoji_label.setText(emojiArray[0]) 
        elif value < 32:
            emoji_label.setText(emojiArray[1]) 
        elif value < 48:
            emoji_label.setText(emojiArray[2]) 
        elif value < 64:
            emoji_label.setText(emojiArray[3]) 
        elif value < 80:
            emoji_label.setText(emojiArray[4]) 
        else:
            label.setText("Activating")  
            emoji_label.setText(emojiArray[5])  # happy face changer
    
    else:
        timer.stop()  # Stop the timer when progress reaches 100
        button.setEnabled(True)  # enable the 
        window.close()
        curentEmotionWindow()
        
       

# Object to execute
app = QApplication([])

# Create the main window
window = QWidget()
window.setWindowTitle("Expression Doctor")
window.setStyleSheet("background-color: #f4f4f9;")  # Light background color

# Label
label = QLabel("Welcome to the Expression Doctor")
label.setWordWrap(True)  #Wrapping for text
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
font = QFont("Arial", 18, QFont.Weight.Bold)  # Larger font size
label.setFont(font)

# Emoji label (added for displaying the emoji)
emoji_label = QLabel(None)
emoji_label.setFont(QFont("Arial", 24))  # Increase font size
emoji_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center emoji

# Button
button = QPushButton("START")

# Button size,colour,font
button.setStyleSheet("""
    QPushButton {
        background-color: #4CAF50; 
        color: white; 
        border-radius: 12px;
        padding: 10px 20px;
        font-size: 16px;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
""")

# Progress bar
progressBar = QProgressBar()
progressBar.setRange(0, 100)  
progressBar.setValue(0)  
progressBar.setTextVisible(False) # needed so u dont see numbers


# Layout
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(emoji_label)  # EMOJIISS !!
layout.addWidget(button)
layout.addWidget(progressBar)

# Button 
button.clicked.connect(on_button_click)

# Timer
timer = QTimer()
timer.timeout.connect(update_progress)

# Centers Window
window.setLayout(layout)
window.setMinimumSize(400, 300)  
window.setStyleSheet("QWidget {border-radius: 15px;}")  # rounded CORNERS !!

# Show window NEEDED
window.show()

# Run the NEEDED
app.exec()


