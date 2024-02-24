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

#VERIFY USER IS REDIRECT TO THE CORRECT URL WITH SPECIFIC INFORMATION (EXAMPLE:JOHN)
driver.find_element(By.ID,"username").click()
driver.find_element(By.ID,"username").send_keys("John")
driver.find_element(By.XPATH,"//button[contains(text(),'Go')]").click()
time.sleep(3)

FoundRepos = driver.find_element(By.XPATH,"//p[@class='repo-amount']")
Repoamount = FoundRepos.text
print(f"{'Number of reports: '}{Repoamount}")

#VERIFY CLICK ON THE RESULT
PageURLRedirect = driver.find_element(By.XPATH,"//a[@href='https://github.com/john/acts-as-taggable-on']")
PageURLRedirect.click()
time.sleep(3)
PageText = driver.find_element(By.LINK_TEXT,"acts-as-taggable-on")

if(PageURLRedirect.text == "acts-as-taggable-on"):
    print("Page displayed is correct")
else:
    print("Page Displayed is not correct")

time.sleep(5)
driver.close()

