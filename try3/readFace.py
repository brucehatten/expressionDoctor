from deepface import DeepFace


def readF(file):
    face = DeepFace.analyze(file, actions=['emotion'])
    emotions = face[0]['emotion']
    emotions['happy'] *= 1.2  # Boost happiness
    emotions['sad'] *= 0.8
    emotions['angry'] *= 1.2     # Reduce sadness
    adjusted_mood = max(emotions, key=emotions.get)
    return "Detected mood:", adjusted_mood
    #return adjusted_mood



