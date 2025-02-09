# expressionDoctor
ReadMe


The Expression Doctor is an application designed to assist individuals in managing emotion. By leveraging real-time emotion detection and interactive feedback, the application helps users become more aware of their emotional state, particularly anger, and helps them take back control.

 Emotion Detection:
Uses a webcam to detect the user's facial expressions 
Identifies emotions such as anger, sadness, fear, disgust, and happiness.

Calming Intervention:
Automatically opens a calming YouTube video using Selenium when the anger, disgust or sadness expressions are identified three times in a row.
The video is designed to help the user relax and regain emotional balance.

What did we use ?
Built using Python with PyQt6 for the GUI and OpenCV for real-time video processing.
Compatible with Windows, macOS, and Linux.








How It Works
Start the Application:
Launch the application and click the "START" button to begin
Emotion Detection:
The application uses your webcam to analyze your facial expressions 
Anger Meter:
Every time an "upset" emotion is detected, it adds up. While three in a row moves you to the next step. Neutral or happy emotions cancels out an angry emotion
Calming Intervention:
When there are three anger emotion moments detected, the application automatically opens a calming YouTube video in your default browser.
(In our case we used a video of cute puppies)
The video plays for 30 seconds, after which the browser window closes.

Libraries Used
PyQt6
opencv-python
deepface
selenium

Hardware Necessary
A working webcam






