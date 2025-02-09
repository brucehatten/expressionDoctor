from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QProgressBar
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QTimer
#import mainTest
import threading

# Emojis for the progress bar stages
sadEmoji = "😭"
fearEmoji = "😱"
angryEmoji = "😡"
disgustEmoji = "🤢"
neutralEmoji = "😐"
happyEmoji = "😊"

# Array of emojis to cycle through
emojiArray = [sadEmoji, fearEmoji, angryEmoji, disgustEmoji, neutralEmoji, happyEmoji]

# Global variable to store the new window
new_window = None

# Function that creates the second window to show the "Current Emotion"
def currentEmotionWindow():
    global new_window  # Use the global variable to store the new window
    print("Opening new window...")  # Debugging statement

    # Create a new QWidget for the second window
    new_window = QWidget()
    new_window.setWindowTitle("Current Emotion")  # Set window title
    new_window.setGeometry(100, 100, 300, 200)  # Position and size
    new_window.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)  # Keep on top of other windows
    new_window.setStyleSheet("background-color: #f4f4f9;")  # Light background color

    # Add an emoji label to the new window
    emoji_label_current = QLabel(emojiArray[5], new_window)  # Set the happy emoji
    emoji_label_current.setFont(QFont("Arial", 40))  # Font size
    emoji_label_current.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the emoji

    # Layout and adding the label to the new window
    layout = QVBoxLayout()
    layout.addWidget(emoji_label_current)
    new_window.setLayout(layout)

    # Show the new window
    new_window.show()

def displayEmotion(emotion):
    emoji_label_current = QLabel(emotion, new_window)
    layout = QVBoxLayout()
    layout.addWidget(emoji_label_current)
    new_window.setLayout(layout)
    new_window.show()


# Function that gets called when the "START" button is clicked
def on_button_click():
    label.setText("LOADING... :)")  # Update the label text to "LOADING"
    button.setDisabled(True)  # Disable the button during loading
    progressBar.setValue(0)  # Reset the progress bar
    


    # Start the timer to simulate loading
    # t1 = threading.Thread(target=timer1)
    t2 = threading.Thread(target=runMainTest, daemon=True)
    timer1()
    

    # t1.start()
    t2.start()

    # t1.join()
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
        timer.stop()  # Stop the timer when progress reaches 100
        button.setEnabled(True)  # Enable the button again
        window.hide()  # Hide the main window instead of closing it

        # Directly call the function to open the new window
        currentEmotionWindow()


def main():
    global app, window, label, button, timer, emoji_label, progressBar
    
    # Main application object


    app = QApplication([])

    # Create the main window
    window = QWidget()
    window.setWindowTitle("Expression Doctor")  # Set main window title
    window.setStyleSheet("background-color: #f4f4f9;")  # Light background color
    window.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    # Label that greets the user
    label = QLabel("Welcome to the Expression Doctor")
    label.setWordWrap(True)  # Wrap text if it exceeds the available space
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the label text
    font = QFont("Arial", 18, QFont.Weight.Bold)  # Set font size and style
    label.setFont(font)

    # Emoji label that will change based on the progress bar
    emoji_label = QLabel(emojiArray[5])  # Initialize with happy emoji
    emoji_label.setFont(QFont("Arial", 24))  # Increase font size for emoji
    emoji_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center emoji

    # The "START" button that triggers the progress bar
    button = QPushButton("START")

    # Button style: background color, text color, padding, font, and hover effect
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

    # Set window layout and appearance
    window.setLayout(layout)
    window.setMinimumSize(400, 300)  # Set the minimum window size
    window.setStyleSheet("QWidget {border-radius: 15px;}")  # Apply rounded corners to the window

    # Show the main window
    window.show()

    # Start the application's event loop
    app.exec()





if __name__ == "__main__":
    main()