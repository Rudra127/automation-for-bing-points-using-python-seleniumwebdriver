#this code is used for the automatic search for bing points using python
#Tip use different VPN for more points 
from selenium import webdriver #pip install selenium
from selenium.webdriver.common.keys import Keys
import random,string
import time
'''---this function is used to gernrate the random string---'''
def generate_random_string(length):
    # Generate a string of specified length containing lowercase and uppercase letters, digits, and punctuation
    random_string = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    return random_string


'''---webdriver edge---'''
#here in this driver variable add your edge webdriver path (Note= the webdriver exe file must be with program file
driver= webdriver.Edge('C:\\Users\\praja\\OneDrive\\Documents\\nothing\\msedgedriver.exe')
driver.get("https://www.bing.com/")
driver.maximize_window()
driver.implicitly_wait(100)
# set time.sleep as per your requirement
time.sleep(30)
#set the range as per your search count the daily limit in the edge for level 1 is 30 means you have to put 10 for level 2 = 30 
for i in range(40):
    search = driver.find_element("xpath",'//*[@id="sb_form_q"]') #here add your xpath for the search box 
    search.send_keys(Keys.BACKSPACE)
    search.send_keys(generate_random_string(5))
    search.send_keys(Keys.ENTER)
    time.sleep(3)
time.sleep(20)
