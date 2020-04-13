from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
import time


def Find_URL():
    # Get what the user wants to search
    result = input("What would you like to search for on Amazon?" + "\n")

    chromedriver = "C:\\Users\\laugh\\Documents\\PythonDriver\\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(chromedriver, options=options)
    driver.get('https://www.amazon.com/')
    search = driver.find_element_by_id("twotabsearchtextbox")

    # Get the result and search for
    search.send_keys(result, Keys.ENTER)
    #time.sleep(30)
    search = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/span[8]/div/div/span/div/div/ul/li[2]/a').get_attribute('href')
    driver.close()
    return search
    
