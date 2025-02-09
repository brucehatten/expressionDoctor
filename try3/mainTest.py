import camera
import UI
from readChrome import browser

def main():
    chrome = browser()
    UI.currentEmotionWindow()
    camera.imageReplace(chrome)
    chrome.heal()

if __name__ == "__main__":
    main()