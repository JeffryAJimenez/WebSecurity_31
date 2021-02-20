import requests, bs4, re

url = 'https://2019shell1.picoctf.com/problem/37829/flag'

res = requests.get(url, headers={"User-Agent": "picobrowser"})
soup = bs4.BeautifulSoup(res.text, "html.parser")

flag = soup.find("code")
result = re.findall('\{(.+)\}', flag.string)[0]

print(result)
