import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

def fp_mn():
    print("hi")
    PATH="C:\SeleniumDrivers\chromedriver.exe"
    driver=webdriver.Chrome(PATH)
    driver.get("https://www.flipkart.com")
    time.sleep(100000)
    driver.quit()