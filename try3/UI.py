from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QProgressBar
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QTimer, QObject, pyqtSignal
import threading
import time

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
emoji_label = None
replace_label = None
button = None
progressBar = None
label = None
timer = None
app = None
window = None

class EmotionSignal(QObject):
    emotion_detected = pyqtSignal(str, str)  # Signal to notify the detected emotion

def currentEmotionWindow():
    global new_window, new_progress_bar, new_timer, emoji_label, replace_label
    print("Opening new window...")  # Debugging statement

    # Create a new QWidget for the second window
    new_window = QWidget()
    new_window.setWindowTitle("Current Emotion")  # Set window title
    new_window.setGeometry(100, 100, 300, 200)  # Position and size
    new_window.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)  # Keep on top of other windows
    new_window.setStyleSheet("background-color: black;")  # Set background color to black

    # Label that will display the emotion text
    replace_label = QLabel(None, new_window)
    replace_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))  # Font size and weight
    replace_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the text
    replace_label.setStyleSheet("color: white;")  # Text color white

    # Emoji label for the progress bar stages
    emoji_label = QLabel(happyEmoji, new_window)  # Default smiley emoji
    emoji_label.setFont(QFont("Arial", 40))  # Set large font size for emoji
    emoji_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the emoji
    emoji_label.setStyleSheet("color: white;")  # Emoji color white

    # Progress bar to show the loading progress
    new_progress_bar = QProgressBar(new_window)
    new_progress_bar.setRange(0, 100)  # Set range from 0 to 100
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

    # Layout to arrange widgets in the window
    layout = QVBoxLayout()
    layout.addWidget(replace_label)  # Add the emotion text label
    layout.addWidget(emoji_label)  # Add the emoji label
    layout.addWidget(new_progress_bar)  # Add the progress bar
    new_window.setLayout(layout)

    # Show the new window
    new_window.show()

    # Start the progress bar timer
    new_timer = QTimer()
    new_timer.timeout.connect(update_progress)  # Update progress bar on timeout
    new_timer.start(50)  # Update every 50ms

def update_progress():
    value = new_progress_bar.value()
    if value < 100:
        new_progress_bar.setValue(value + 1)  # Increment progress by 1
        # Change emojis based on the progress value
        if value < 16:
            emoji_label.setText(emojiArray[0])  # Sad emoji
        elif value < 32:
            emoji_label.setText(emojiArray[1])  # Fear emoji
        elif value < 48:
            emoji_label.setText(emojiArray[2])  # Angry emoji
        elif value < 64:
            emoji_label.setText(emojiArray[3])  # Disgust emoji
        elif value < 80:
            emoji_label.setText(emojiArray[4])  # Neutral emoji
        else:
            replace_label.setText("Activating")  # Show "Activating" when near 100%
            emoji_label.setText(emojiArray[5])  # Happy emoji

    else:
        new_timer.stop()  # Stop the timer when progress reaches 100%
        new_window.hide()  # Hide the window

        # Here, you can trigger further actions after the progress bar completes
        # Example: Call the emotion detection function
        emotion_signal.emotion_detected.emit('happy', 'You are feeling happy!')

def displayEmotion(emotion, emotionText):
    global emoji_label, replace_label
    # Update the emotion and text in the emotion window
    emoji_label.setText(emotion)
    replace_label.setText(emotionText)
    print(f"Emotion detected: {emotion}")

def on_button_click():
    label.setText("LOADING...")  # Update the label text to "LOADING"
    button.setDisabled(True)  # Disable the button during loading
    progressBar.setValue(0)  # Reset the progress bar

    # Start the background thread to run the main test
    t2 = threading.Thread(target=runMainTest, daemon=True)
    t2.start()

def runMainTest():
    import mainTest  # Import the main test file
    mainTest.main()  # Call the main function from the test file

def emotion_signal_emit():
    emotion_signal.emotion_detected.emit("😊", "You are happy!")  # Example emotion signal emission

def main():
    global app, window, label, button, progressBar, timer, emotion_signal

    # Main application object
    app = QApplication([])

    # Setup emotion signal connection
    emotion_signal = EmotionSignal()
    emotion_signal.emotion_detected.connect(displayEmotion)  # Connect emotion signal to displayEmotion

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
    emoji_label = QLabel(happyEmoji)  # Initialize with happy emoji
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
    button.clicked.connect(on_button_click)  # Connect button click to on_button_click

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

    # Layout to organize widgets in the window
    layout = QVBoxLayout()
    layout.addWidget(label)  # Add the main label
    layout.addWidget(emoji_label)  # Add the emoji label
    layout.addWidget(button)  # Add the "START" button
    layout.addWidget(progressBar)  # Add the progress bar

    # Set the layout for the main window
    window.setLayout(layout)
    window.setMinimumSize(400, 300)  # Set the minimum window size
    window.setStyleSheet("QWidget {border-radius: 15px;}")  # Apply rounded corners to the window

    # Show the main window
    window.show()

    # Execute the application
    app.exec()

if __name__ == "__main__":
    main()
