from lib2to3.pgen2 import driver
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

# WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
#     (By.XPATH, "/html/body/div/main/div/ul[2]/li[1]/a"))).click()

wait = WebDriverWait(driver, 5)
link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Introduction"))).click()

# element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div/ul[2]/li[1]/a")))
# element.click()

# WebDriverWait(driver, 2000).until()
# elem = browser.find_element(By.XPATH, value='/html/body/div/main/div/ul[2]/li[1]/a')
# elem.click()
