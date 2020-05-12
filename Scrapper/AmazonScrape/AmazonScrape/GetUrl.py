from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
import time
import logging
from selenium.webdriver.remote.remote_connection import LOGGER as seleniumLogger



def Find_URL(name):
    # Get what the user wants to search
    seleniumLogger.setLevel(logging.WARNING)
    chromedriver = "C:\\Users\\laugh\\Documents\\PythonDriver\\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(chromedriver, options=options)
    if(name == "amazon"):
        result = input("\n\n" + "What would you like to search for on Amazon?" + "\n")
        driver.get('https://www.amazon.com/')
        time.sleep(3)
        search = driver.find_element_by_id("twotabsearchtextbox")
        # Get the result and search for
        search.send_keys(result, Keys.ENTER)
        search = driver.current_url
        print(search)
        driver.close()
    else:
        result = input("\n\n" + "What would you like to search for on Ebay?" + "\n")
        driver.get('https://www.ebay.com')
        search = driver.find_element_by_id("gh-ac")
        search.send_keys(result, Keys.ENTER)
        search = driver.current_url
        print(search)
        driver.close()
    return search
    
