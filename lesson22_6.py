# работа с выпадающим списком
from selenium import webdriver
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x1 = browser.find_element_by_css_selector('#input_value').text
    input1 = browser.find_element_by_css_selector('#answer')
    print(x1)
    input1.send_keys(calc(x1))
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    btn = browser.find_element_by_css_selector('button[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    btn.click()

finally:
    time.sleep(10)
    browser.quit()