from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import time
import os

USER_GMAIL = "armloveyou252@hotmail.com" 
PASSWORD_GMAIL = "@Armandsoft87"


chrome_driver = "C:\Developer\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://tinder.com")


time.sleep(2)
accept = driver.find_element_by_xpath('//*[@id="q-1330521921"]/div/div[2]/div/div/div[1]/div[1]/button')
accept.click()

time.sleep(2)
login = driver.find_element_by_xpath('//*[@id="q-1330521921"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()

time.sleep(2)
google_login = driver.find_element_by_xpath('//*[@id="q1236064299"]/div/div/div[1]/div/div[3]/span/div[2]/button')
google_login.click()

time.sleep(2)
gg_login_window = driver.window_handles[1]
switch_to_gg_login = driver.switch_to.window(gg_login_window)

time.sleep(2)
google_login_gmail = driver.find_element_by_xpath('//*[@id="email"]')
google_login_gmail.send_keys(USER_GMAIL)

time.sleep(2)
google_login_password = driver.find_element_by_xpath('//*[@id="pass"]')
google_login_password.send_keys(PASSWORD_GMAIL)
google_login_password.send_keys(Keys.ENTER)

time.sleep(3)
tinder_window = driver.window_handles[0]
switch_to_tinder = driver.switch_to.window(tinder_window)

time.sleep(5)
allow = driver.find_element_by_xpath('//*[@id="q1236064299"]/div/div/div/div/div[3]/button[1]')
allow.click()

time.sleep(3)
enable_not = driver.find_element_by_xpath('//*[@id="q1236064299"]/div/div/div/div/div[3]/button[2]')
enable_not.click()

for i in range(100):

    time.sleep(3)
    click_dismiss = driver.find_element_by_xpath('//*[@id="q-1330521921"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
    click_dismiss.click()
    
 

    # except:
    #     click_dont_add_home_screen = driver.find_element_by_xpath('//*[@id="q1236064299"]/div/div/div[2]/button[2]')
    #     click_dont_add_home_screen.click()