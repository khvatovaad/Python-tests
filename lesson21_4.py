from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_css_selector('#input_value')
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(calc(x.text))
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()
    btn = browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
    time.sleep(10)
    browser.quit()