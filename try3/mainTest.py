import camera
from readChrome import browser

def main():
    chrome = browser()
    camera.imageReplace(chrome)
    chrome.heal()

if __name__ == "__main__":
    main()