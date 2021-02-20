import requests, bs4, re, jsbeautifier

url = 'https://2019shell1.picoctf.com/problem/37886/'
pattern = re.compile("if\s\((.+)\)")
flag = dict()

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, "html.parser")
script = soup.find_all("script")[1]

#find the split distance and parse it
split_distance = int(re.findall('split=0x(\d)', script.string)[0])
beauty = jsbeautifier.beautify(script.string)

arr_0x5a46 = re.search('var\s_0x5a46\s=\s\[(.+)\];', beauty)[1]
arr_0x5a46 = arr_0x5a46.split(',')
for x in range(len(arr_0x5a46)):
    arr_0x5a46[x] = re.search('\'(.+)\'', arr_0x5a46[x])[1]
flg_fragments = pattern.findall(beauty)

for frament in flg_fragments:
    
    #find the string and the boundries
    subs =  re.search('\s_0x4b5b\(\'(.+)\'\)|=\s\'(.+)\'', frament)[1]
    if subs is None:
        subs = re.search('\s_0x4b5b\(\'(.+)\'\)|=\s\'(.+)\'', frament)[2]
    boundries = re.search(']\((.+)\)\s=', frament)[1]
    boundries = boundries.split(',')
    
    index = 0
    for boundrie in boundries:
        total = 1
        temp = boundrie.split('*')
        for value in temp:
            if 'split' in value:
                total *= split_distance;
            else:
                x = int(value, 0)
                total *= x
        boundries[index] = total
        index += 1

    if '0x' in subs:
        index = int(subs, 0) + 5 if (int(subs, 0) + 5 < len(arr_0x5a46)) else int(subs, 0) + 5 - len(arr_0x5a46)
        subs = arr_0x5a46[index]
    
    #check if the 1 boundry is missing and replace acorndingly
    if len(boundries) == 1:
        if int(boundries[0]) > 0:
            boundries.insert(0, 1)
        else:
            boundries.append(1)
    
    cursor = 0;
    for x in range(int(boundries[0]), int(boundries[1])):
        if not(x in flag) and cursor < len(subs):
            flag[x] = subs[cursor]
        cursor += 1

result = ''
for k in sorted (flag):
    result += flag[k]


print(re.findall('\{(.+)\}', result)[0])



