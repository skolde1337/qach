from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))



browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/explicit_wait2.html")


# говорим WebDriver искать каждый элемент в течение 5 секунд

# button = WebDriverWait(browser, 12).until(
# EC.text_to_be_present_in_element(By.ID, "book"), "100")
# button.click()

wait = WebDriverWait(browser, 12)
element = wait.until(EC.text_to_be_present_in_element((By.ID,"price"), "$100"))
button = browser.find_element_by_class_name('btn-primary')
button.click()


x_element = browser.find_element_by_id("input_value")
a = x_element.text
x = int(a)
y = calc(x)

browser.execute_script("return arguments[0].scrollIntoView(true);", button)
input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

button = browser.find_element_by_css_selector('[type="submit"]')
button.click()
