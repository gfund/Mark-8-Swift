from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import time
def imageget(url):
    print(url)
    driver = webdriver.Firefox()
    driver.get(url)
   
   
    driver.save_screenshot('websearch.png')
   
    driver.quit()