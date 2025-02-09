from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QProgressBar
from PyQt6.QtGui import QFont, QImage, QPixmap
from PyQt6.QtCore import Qt, QTimer, pyqtSignal, QObject
import threading
import cv2
from deepface import DeepFace

# Emojis for the emotions
emojis = {
    "sad": "😭",
    "fear": "😱",
    "angry": "😡",
    "disgust": "🤢",
    "neutral": "😐",
    "happy": "😊"
}

# Global variables
new_window = None
emoji_label_current = None
cap = None  # Video capture object

# Emotion detection thread
class EmotionDetectionThread(QObject):
    emotion_detected = pyqtSignal(str)  # Signal to emit the detected emotion

    def run(self):
        global cap
        cap = cv2.VideoCapture(0)  # Open the default camera
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Analyze the frame for emotions
            try:
                result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                dominant_emotion = result[0]['dominant_emotion']
                self.emotion_detected.emit(dominant_emotion)
            except Exception as e:
                print(f"Error in emotion detection: {e}")

            # Display the camera feed (optional)
            cv2.imshow("Camera Feed", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
                break

        cap.release()
        cv2.destroyAllWindows()

# Function that creates the second window to show the "Current Emotion"
def currentEmotionWindow():
    global new_window, emoji_label_current
    new_window = QWidget()
    new_window.setWindowTitle("Current Emotion")
    new_window.setGeometry(100, 100, 300, 200)
    new_window.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
    new_window.setStyleSheet("background-color: #f4f4f9;")

    emoji_label_current = QLabel(emojis["happy"], new_window)
    emoji_label_current.setFont(QFont("Arial", 40))
    emoji_label_current.setAlignment(Qt.AlignmentFlag.AlignCenter)

    layout = QVBoxLayout()
    layout.addWidget(emoji_label_current)
    new_window.setLayout(layout)
    new_window.show()

# Function to display the detected emotion
def displayEmotion(emotion):
    global new_window, emoji_label_current
    if new_window is not None and emoji_label_current is not None:
        emoji_label_current.setText(emojis.get(emotion, "❓"))  # Update the emoji
        new_window.show()

# Function that gets called when the "START" button is clicked
def on_button_click():
    label.setText("LOADING... :)")
    button.setDisabled(True)
    progressBar.setValue(0)

    # Start the progress bar timer
    timer1()

    # Start emotion detection in a separate thread
    emotion_thread = EmotionDetectionThread()
    emotion_thread.emotion_detected.connect(displayEmotion)
    threading.Thread(target=emotion_thread.run, daemon=True).start()

def timer1():
    timer.start(50)

# Function to update the progress bar and change emojis based on progress
def update_progress():
    value = progressBar.value()
    if value < 100:
        progressBar.setValue(value + 1)
        if value < 16:
            emoji_label.setText(emojis["sad"])
        elif value < 32:
            emoji_label.setText(emojis["fear"])
        elif value < 48:
            emoji_label.setText(emojis["angry"])
        elif value < 64:
            emoji_label.setText(emojis["disgust"])
        elif value < 80:
            emoji_label.setText(emojis["neutral"])
        else:
            label.setText("Activating")
            emoji_label.setText(emojis["happy"])
    else:
        timer.stop()
        button.setEnabled(True)
        window.hide()
        currentEmotionWindow()

def main():
    global app, window, label, button, timer, emoji_label, progressBar
    app = QApplication([])

    # Create the main window
    window = QWidget()
    window.setWindowTitle("Expression Doctor")
    window.setStyleSheet("background-color: #f4f4f9;")
    window.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    # Label that greets the user
    label = QLabel("Welcome to the Expression Doctor")
    label.setWordWrap(True)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    font = QFont("Arial", 18, QFont.Weight.Bold)
    label.setFont(font)

    # Emoji label that will change based on the progress bar
    emoji_label = QLabel(emojis["happy"])
    emoji_label.setFont(QFont("Arial", 24))
    emoji_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # The "START" button
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

    # Progress bar
    progressBar = QProgressBar()
    progressBar.setRange(0, 100)
    progressBar.setValue(0)
    progressBar.setTextVisible(False)

    # Layout
    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(emoji_label)
    layout.addWidget(button)
    layout.addWidget(progressBar)
    window.setLayout(layout)
    window.setMinimumSize(400, 300)
    window.setStyleSheet("QWidget {border-radius: 15px;}")

    # Connect button click event
    button.clicked.connect(on_button_click)

    # Timer for updating the progress bar
    timer = QTimer()
    timer.timeout.connect(update_progress)

    # Show the main window
    window.show()

    # Start the application's event loop
    app.exec()

if __name__ == "__main__":
    main()

