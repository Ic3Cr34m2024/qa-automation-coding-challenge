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

#VERIFY INFORMATION RESULTS POSITVE SCENARIO
driver.find_element(By.ID,"username").click()
driver.find_element(By.ID,"username").send_keys("John")
driver.find_element(By.XPATH,"//button[contains(text(),'Go')]").click()
time.sleep(3)

FoundRepos = driver.find_element(By.XPATH,"//p[@class='repo-amount']")
Repoamount = FoundRepos.text
print(f"{'Number of reports: '}{Repoamount}")

#VERIFY THE SEARCH RETURN CONTENT
RepoUrl = driver.find_element(By.XPATH,"(//li[@class='repo-row'])[1]")
print(RepoUrl.is_displayed())

if(RepoUrl.is_displayed()==True):
    print("This User contains at least one report")
else:
     print("user does not have any report") 




driver.close()