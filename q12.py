from selenium import webdriver
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

input1 = browser.find_element_by_css_selector('[placeholder="Enter first name"]')
input1.send_keys("Ivan")

input1 = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
input1.send_keys("Ivanov")

input1 = browser.find_element_by_css_selector('[placeholder="Enter email"]')
input1.send_keys("sasha@email.ru")

input1 = browser.find_element_by_css_selector('[type="file"]')
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
input1.send_keys(file_path)

button = browser.find_element_by_class_name('btn-primary')
button.click()