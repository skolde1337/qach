from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element_by_class_name('trollface.btn.btn-primary')
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element_by_id("input_value")
a = x_element.text
x = int(a)
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

button = browser.find_element_by_class_name('btn-primary')
button.click()