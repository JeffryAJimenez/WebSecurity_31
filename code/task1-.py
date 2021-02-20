import requests, bs4, re

url = 'https://2019shell1.picoctf.com/problem/49886/'
pattern = re.compile("\(.+\.substring(\(.+\))\s={2}\s(.+)\)")
flag = dict()

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, "html.parser")

script = soup.find_all("script")[1]

#find the split distance and parse it
split_distance = int(re.findall('split\s=\s(\d)', script.string)[0])

flg_fragments = pattern.findall(script.string)

for frament in flg_fragments:
    
    #find the string and the boundries
    subs =  re.search('\'(.+)\'',frament[1])[1]
    boundries = re.findall('\d', frament[0])
    
    #check if the 1 boundry is missing and replace acorndingly
    if len(boundries) == 1:
        if int(boundries[0]) > 0:
            boundries.insert(0, 1)
        else:
            boundries.append(1)
    
    cursor = 0;
    for x in range(int(boundries[0]) * split_distance, int(boundries[1])*split_distance):
        if not(x in flag) and cursor < len(subs):
            flag[x] = subs[cursor]
        cursor += 1

result = ''
for k in sorted (flag):
    result += flag[k]


print(re.findall('\{(.+)\}', result)[0])


