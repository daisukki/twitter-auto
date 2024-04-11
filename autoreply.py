import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'text')))
email_field.send_keys("#user") #place your user here 
email_field.send_keys(Keys.ENTER)

password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
password_field.send_keys("#password") #place your password here 
password_field.send_keys(Keys.ENTER)

time.sleep(4)

comentarios = ['#1', '#2', '#3'] # ... 

def find_and_click(xpath):
    try:
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
    except (ElementClickInterceptedException, StaleElementReferenceException):
        find_and_click(xpath)

def send_random_comment():
    comment_box = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='tweetTextarea_0']")))
    comment_box.send_keys(random.choice(comentarios))
    send_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='tweetButton']")))
    send_button.click()

search_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@data-testid="SearchBox_Search_Input"]')))
search_field.send_keys('#param')  
search_field.send_keys(Keys.ENTER)

time.sleep(4)

while True:
    try:
        find_and_click("//div[@data-testid='retweet']/div") 
        time.sleep(1)  

        find_and_click("//div[@data-testid='retweetConfirm']/div")  
        time.sleep(2)  

        like_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='like']/div")))
        like_button.click()  

        time.sleep(2)

        comment_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='reply']")))
        comment_button.click() 

        time.sleep(1)

        send_random_comment()

    except Exception as e:
        driver.quit()
        print("Ocorreu um erro:", e)
        break