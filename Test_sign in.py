from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://www.saucedemo.com'
username = 'standard_user'
password = 'secret_sauce'

def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver

def open_page(driver, url):
    driver.get(url)

def get_element_by_id(driver, locator):
    return driver.find_element(By.ID, locator)

def element_send_keys(driver, locator, text):
    element = get_element_by_id(driver, locator)
    element.send_keys(text)

def element_click(driver, locator):
    element = get_element_by_id(driver, locator)
    element.click()

def login(driver, login, password):
    element_send_keys(driver, 'user-name', login)
    element_send_keys(driver, 'password', password)
    element_click(driver, 'login-button')

driver = get_driver()
open_page(driver, URL)
login(driver=driver, login=username, password=password)

driver.quit()

