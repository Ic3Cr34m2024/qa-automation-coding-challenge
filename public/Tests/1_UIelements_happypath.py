from tkinter import BROWSE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
#from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
import random
import time
import re
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))


Github = "http://localhost:3000/"
driver.get(Github)
driver.maximize_window()
time.sleep(3)

#VERIFY TITLE OF THE PAGE
PageTitle = driver.find_element(By.XPATH, "//h1[contains(.,'Get Github Repos')]")  
PageTitletxt = PageTitle.text
print(f"{'Title of the Page: '}{PageTitletxt}")  
assert PageTitle.text == "Get Github Repos"

#VERIFY USERNAME FIELD IS PRESENTED
UserNameField= driver.find_element(By.ID,"username")
print(UserNameField.is_displayed())

if(UserNameField.is_displayed()==True):
    print("UserName Field presented")
else:
    print("UserName is not presented")

#VERIFY GO BUTTON IS PRESENTED
GoButton = driver.find_element(By.XPATH, "//button[@class='submit'][contains(.,'Go')]") 
print(GoButton.is_displayed())

if(GoButton.is_displayed()==True):
    print("Go Button presented")
else:
    print("Go Button  is not presented")

#VERIFY SUCCESS RESULT
driver.find_element(By.ID,"username").click()
UserNameField.send_keys("john")
driver.find_element(By.XPATH,"//button[contains(text(),'Go')]").click()
time.sleep(3)

Successresult = driver.find_element(By.XPATH,"//strong[contains(text(),'Success!')]")
SuccessResultTxt = Successresult.text
print(f"{'Message displayed: '}{SuccessResultTxt}") 
print("User Found and Results displayed")
time.sleep(3)


driver.close()
