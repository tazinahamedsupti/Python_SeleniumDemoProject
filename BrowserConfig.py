from selenium import webdriver

#Chrome Config
driver_Chrome = webdriver.Chrome(executable_path="C:\\Users\\Splinter Tracer\\PycharmProjects\\Python_SeleniumDemoProject\\BrowserDrivers\\chromedriver.exe")
print("Chrome Driver Configures Successfully!")

#Open Test Website
driver_Chrome.get("https://www.google.com/")
print("Link opened Successfully!")

#Maximize Window
driver_Chrome.maximize_window()
print("Maximum Window Successfull!")

#Close Current/Active Tab
driver_Chrome.close()
print("Active Tab Closed Successfully!")

#Terminate Browser
driver_Chrome.quit()
print("Browser Quit Successfull!")

#Firefox Confiq
driver_Firefox = webdriver.Firefox(executable_path="C:\\Users\\Splinter Tracer\\PycharmProjects\\Python_SeleniumDemoProject\\BrowserDrivers\\geckodriver.exe")
driver_Firefox.get("https://www.google.com/")
driver_Firefox.quit()

print("Test Done!!!")



