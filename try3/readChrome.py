from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class browser:

    def __init__(self):
        
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # Open in full screen
        options.add_argument("--disable-gpu")  # Disable GPU acceleration
        options.add_argument("--disable-software-rasterizer")  
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.google.com")
        self.happyLinks = [r'https://youtu.be/BYh3Gykv90w?si=yITRu0vHVzjjvH5g&t=8996&fs']
        self.badLinks = [r'x.com', r'instagram']

    def url(self):
        current_tab_url = self.driver.current_url
        return current_tab_url
    
    def isBad(self):
        url = self.url()
        for link in self.badLinks:
            if link in url:
                return True
        return False


    def quit(self):
        self.driver.quit()

    def heal(self):
        val = self.happyLinks[0]
        wait = WebDriverWait(self.driver, 10)
        self.driver.get(val)
        sleep(30)
        #wait.until(EC.url_contains("youtube.com/watch"))
        #page_source = self.driver.page_source
        