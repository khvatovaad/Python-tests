# работа с выпадающим списком
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'

def func(x, y):
    return str(int(x)+int(y))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    a = browser.find_element_by_id('num1').text
    b = browser.find_element_by_id('num2').text
    c = func(a, b)
    select = browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("[value='" + c + "']").click()
    btn = browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
    time.sleep(10)
    browser.quit()