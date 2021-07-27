# работа с выпадающим списком
from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_tag_name("input[name='firstname']")
    input1.send_keys('test')
    input2 = browser.find_element_by_tag_name("input[name='lastname']")
    input2.send_keys('test')
    input3 = browser.find_element_by_tag_name("input[name='email']")
    input3.send_keys('test@mail.ru')

    current_dir = os.path.abspath(os.path.dirname('C:\\Users\\khvat\\Desktop\\'))
    file_path = os.path.join(current_dir, 'test.txt')
    file = browser.find_element_by_tag_name("input[name='file']")
    file.send_keys(file_path)
    btn = browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
    time.sleep(10)
    browser.quit()