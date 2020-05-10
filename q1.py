import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 10 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(10)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/math.html")
time.sleep(5)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
textarea = driver.find_element_by_css_selector(".textarea")
x_element = browser.find_element_by_*(selector)
x = x_element.text
y = calc(x)


# Напишем текст ответа в найденное поле
textarea.send_keys('y')
time.sleep(10)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(10)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()
