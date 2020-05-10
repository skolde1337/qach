from selenium import webdriver
import time
import math
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input1 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    input1.send_keys("Ivanov")
    input1 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
    input1.send_keys("912030123123")
    # input1 = browser.find_element_by_css_selector('[placeholder="Input your adress"]')
    # input4.send_keys("msc")
    # Отправляем заполненную форму
    button = browser.find_element_by_class_name('btn-default')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()