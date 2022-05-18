from selenium import webdriver

#Chrome Config
driver = webdriver.Chrome(executable_path="C:\\Users\\Splinter Tracer\\PycharmProjects\\Python_SeleniumDemoProject\\BrowserDrivers\\chromedriver.exe")
print("Chrome Driver Configures Successfully!")

#Open website
driver.get("https://www.google.com/")
print("Link opened Successfully!")

#maximize size window
driver.maximize_window()
print("Maximize size window opened!")

#Get maximize window size
max_window_size = driver.get_window_size()
print("Window Size: ", max_window_size)

#Set Window Size
driver.set_window_size(800,500)
windowSetSize = driver.get_window_size()
print("Previously Defined Window Size was 800/500: ", windowSetSize)

print("Test Done!!!")



