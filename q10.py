from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math




try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    frst = browser.find_element_by_id("num1")
    x = frst.text
    scnd = browser.find_element_by_id("num2")
    y = scnd.text
    result = int(x)+int(y)
    text =str(result)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(text)  # ищем элемент с текстом "Python"
    #x_element = browser.find_element_by_tag_name("select").click()

    #reselem = browser.find_element_by_css_selector("[value='{result}']").click()




    # Отправляем заполненную форму
    button = browser.find_element_by_class_name('btn.btn-default')
    button.click()

    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()