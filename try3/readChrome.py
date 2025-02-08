from selenium import webdriver

# Set up Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Open in full screen
driver = webdriver.Chrome(options=options)

# Open a website
driver.get("https://www.google.com")

# Get the current tab URL
current_tab_url = driver.current_url
print("Active Tab URL:", current_tab_url)

# Get the current tab title
current_tab_title = driver.title
print("Active Tab Title:", current_tab_title)

# Close the browser when done
driver.quit()
