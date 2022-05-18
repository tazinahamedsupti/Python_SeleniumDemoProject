from selenium import webdriver

#Chrome Config
driver = webdriver.Chrome(executable_path="C:\\Users\\Splinter Tracer\\PycharmProjects\\Python_SeleniumDemoProject\\BrowserDrivers\\chromedriver.exe")
print("Chrome Driver Configures Successfully!")

#Open website
driver.get("https://www.google.com/")
print("Link opened Successfully!")

#Title verification
expectedTitle = "Google"
actualTitle = driver.title

if expectedTitle == actualTitle:
    print("Title Verification passed!")
else:
    print("Error! Actual Title: "+actualTitle)

#Terminate Browser
driver.quit()
print("Browser Quit Successfull!")

print("Test Done!")