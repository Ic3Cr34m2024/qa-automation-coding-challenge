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

#VERIFY UserName FIELD DOES NOT ACCEPT SPECIAL CHARACTERS
driver.find_element(By.ID,"username").click()
driver.find_element(By.ID,"username").send_keys("%&#$%&")
driver.find_element(By.XPATH,"//button[contains(text(),'Go')]").click()
time.sleep(3)

#VERIFY "ERROR MESSAGE" 
ErrorMessage = driver.find_element(By.CSS_SELECTOR, "body:nth-child(2) div:nth-child(2) div.app main:nth-child(2) > section.message-area")  
SomethingWrongError = ErrorMessage.text
print(f"{'Message displayed: '}{SomethingWrongError}")


driver.close()