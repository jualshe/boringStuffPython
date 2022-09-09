from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

link = browser.find_element(By.LINK_TEXT, 'Introduction')
browser.execute_script("arguments[0].click();", link)
