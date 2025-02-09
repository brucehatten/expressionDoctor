from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QProgressBar
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QTimer
import threading

from PyQt6.QtCore import QObject, pyqtSignal

from PyQt6.QtCore import QObject, pyqtSignal

class EmotionSignal(QObject):
    emotion_detected = pyqtSignal(str, str)  # Signal carrying emoji and emotion text


def setup_signal_connections():
    # Connect the signal to the displayEmotion function
    emotion_signal.emotion_detected.connect(displayEmotion)

emotion_signal = EmotionSignal()

 

def counterBar(count, COUNTERBREAK):

    if count < COUNTERBREAK:
        y = count * (COUNTERBREAK / 100)
        new_progress_bar.setValue(y)  # Increment progress by y
    elif count == COUNTERBREAK:
        new_timer.stop()  # Stop the timer when progress reaches 100
        new_window.hide()

emoji_label = None
replace_label = None

# Emojis for the progress bar stages
sadEmoji = "😭"
fearEmoji = "😱"
angryEmoji = "😡"
disgustEmoji = "🤢"
neutralEmoji = "😐"
happyEmoji = "😊"

# Array of emojis to cycle through
emojiArray = [sadEmoji, fearEmoji, angryEmoji, disgustEmoji, neutralEmoji, happyEmoji]

# Global variables
new_window = None
new_progress_bar = None
new_timer = None

# Function that creates the second window to show the "Current Emotion"
def currentEmotionWindow():
    global new_window, new_progress_bar, new_timer
    print("Opening new window...")  # Debugging statement

    # Create a new QWidget for the second window
    new_window = QWidget()
    new_window.setWindowTitle("Current Emotion")  # Set window title
    new_window.setGeometry(100, 100, 300, 200)  # Position and size
    new_window.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)  # Keep on top of other windows
    new_window.setStyleSheet("background-color: black;")  # Set background color to black

    # ADD WHATEVER TEXT U WANT HERE
    global replace_label
    replace_label = QLabel(None, new_window)
    replace_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))  # FONT ET SIZE
    replace_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # ALIGNMENT
    replace_label.setStyleSheet("color: white;")  # Set text color to white

    # EMOJI STUFF HERE  
    global emoji_label
    emoji_label = QLabel(happyEmoji, new_window)  # Default smiley emoji
    emoji_label.setFont(QFont("Arial", 40))  # Font size
    emoji_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the emoji
    emoji_label.setStyleSheet("color: white;")  # Set emoji color to white

    # PROGESS BAR
    global new_progress_bar
    new_progress_bar = QProgressBar(new_window)
    new_progress_bar.setRange(0, 100)  # Set the range from 0 to 100
    new_progress_bar.setValue(0)  # Set initial value to 0
    new_progress_bar.setTextVisible(False)  # Hide numbers on the progress bar
    new_progress_bar.setStyleSheet("""
        QProgressBar {
            background-color: #333333;  /* Dark gray background */
            border-radius: 5px;        /* Rounded corners */
            height: 20px;              /* Make the progress bar thicker */
        }
        QProgressBar::chunk {
            background-color: #4CAF50; /* Green progress bar */
            border-radius: 5px;        /* Rounded corners */
        }
    """)

    # LAYOUT
    #global replace_label, emoji_label
    layout = QVBoxLayout()
    layout.addWidget(replace_label)  # Add the "Replace Me" label
    layout.addWidget(emoji_label)  # Add the emoji label
    layout.addWidget(new_progress_bar)  # Add the new progress bar
    new_window.setLayout(layout)

    # WINDOW
    new_window.show()

    # PROGRESS BAR
    new_timer = QTimer()
    #new_timer.timeout.connect(counterBar)

    new_timer.start(50)  # UPDATE
    return replace_label


def displayEmotion(emotion, emotionText):
    # currentEmotionWindow()
    global emoji_label, replace_label
    if emoji_label != None:
        emoji_label.setText(emotion)
    if replace_label != None:
        replace_label.setText(emotionText)

    print(f" found {emotion}")
    new_window.show()




# Function to update the progress bar in the new window


# Function that gets called when the "START" button is clicked
def on_button_click():
    label.setText("LOADING...")  # Update the label text to "LOADING"
    button.setDisabled(True)  # Disable the button during loading
    progressBar.setValue(0)  # Reset the progress bar

# Start the timer to simulate loading
    # t1 = threading.Thread(target=timer1)
    t2 = threading.Thread(target=runMainTest, daemon=True)
    timer1()
    

    # # t1.start()
    t2.start()

    # # t1.join()
    # t2.join()

def timer1():
    timer.start(50) 

def runMainTest():
    import mainTest
    mainTest.main()
# Function to update the progress bar and change emojis based on progress
def update_progress():
    value = progressBar.value()
    if value < 100:
        progressBar.setValue(value + 1)  # Increment progress by 1
        if value < 16:
            emoji_label.setText(emojiArray[0])  # Show sad emoji
        elif value < 32:
            emoji_label.setText(emojiArray[1])  # Show fear emoji
        elif value < 48:
            emoji_label.setText(emojiArray[2])  # Show angry emoji
        elif value < 64:
            emoji_label.setText(emojiArray[3])  # Show disgust emoji
        elif value < 80:
            emoji_label.setText(emojiArray[4])  # Show neutral emoji
        else:
            label.setText("Activating")  # Change the label to "Activating"
            emoji_label.setText(emojiArray[5])  # Show happy emoji when near 100%

    else:
        timer.stop()  # STOP TIMER
        #button.setEnabled(True)  # BUTTON ENABLE
        window.hide()  # HIDE MAIN...

        # Directly call the function to open the new window
        #currentEmotionWindow()
    #     t2 = threading.Thread(target=runMainTest, daemon=True)
    

    # # t1.start()
    #     t2.start()

    # t1.join()
    # t2.join()

def main():
    global app, window, label, button, timer, emoji_label, progressBar

    # Main application object
    app = QApplication([])

    currentEmotionWindow()
    setup_signal_connections() 
    # Create the main window
    window = QWidget()
    window.setWindowTitle("Expression Doctor")  # Set main window title
    window.setStyleSheet("background-color: black;")  # Set background color to black

    # Label that greets the user
    label = QLabel("Welcome to the Expression Doctor")
    label.setWordWrap(True)  # Wrap text if it exceeds the available space
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the label text
    font = QFont("Arial", 18, QFont.Weight.Bold)  # Set font size and style
    label.setFont(font)
    label.setStyleSheet("color: white;")  # Set text color to white

    # Emoji label that will change based on the progress bar
    emoji_label = QLabel(emojiArray[5])  # Initialize with happy emoji
    emoji_label.setFont(QFont("Arial", 24))  # Increase font size for emoji
    emoji_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center emoji
    emoji_label.setStyleSheet("color: white;")  # Set emoji color to white

    # The "START" button that triggers the progress bar
    button = QPushButton("START")
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

    

    # Progress bar to show loading progress
    progressBar = QProgressBar()
    progressBar.setRange(0, 100)  # Set the range from 0 to 100
    progressBar.setValue(0)  # Set initial value to 0
    progressBar.setTextVisible(False)  # Hide numbers on the progress bar
    progressBar.setStyleSheet("""
        QProgressBar {
            background-color: #333333;  /* Dark gray background */
            border-radius: 5px;        /* Rounded corners */
            height: 20px;              /* Make the progress bar thicker */
        }
        QProgressBar::chunk {
            background-color: #4CAF50; /* Green progress bar */
            border-radius: 5px;        /* Rounded corners */
        }
    """)
    
    # Layout for organizing widgets in the window
    layout = QVBoxLayout()
    layout.addWidget(label)  # Add the main label
    layout.addWidget(emoji_label)  # Add the emoji label
    layout.addWidget(button)  # Add the "START" button
    layout.addWidget(progressBar)  # Add the progress bar

    # Connect the button click event to the on_button_click function
    button.clicked.connect(on_button_click)

    # Timer for updating the progress bar
    timer = QTimer()
    timer.timeout.connect(update_progress)  # Update progress when the timer times out



    button.clicked.connect(on_button_click)
    


    # Layout

    window.setLayout(layout)
    window.setMinimumSize(400, 300)  # Set the minimum window size
    window.setStyleSheet("QWidget {border-radius: 15px;}")  # Apply rounded corners to the window

    # Main Window
    window.show()
    
    # Execute
    app.exec()

if __name__ == "__main__":
    main()