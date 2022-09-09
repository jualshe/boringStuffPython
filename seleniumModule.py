from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element(By.CSS_SELECTOR, '.main > main:nth-child(1) > div:nth-child(1) > p:nth-child(6)')
print(elem.text)

elem1 = browser.find_element(By.CSS_SELECTOR, 'html')
print(elem1.text)

link = browser.find_element(By.LINK_TEXT, 'Introduction')
browser.execute_script("arguments[0].click();", link)
browser.back()
browser.forward()
browser.refresh()
browser.quit()
