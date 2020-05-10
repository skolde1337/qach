from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

x_element = browser.find_element_by_id("input_value")
a = x_element.text
x = int(a)
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

option1 = browser.find_element_by_id("robotsRule")
option1.click()

button = browser.find_element_by_class_name('btn-primary')
button.click()

assert True