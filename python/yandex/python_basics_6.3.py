"""Module requests"""

# A
from requests import get
from sys import stdin
from requests import post
from json import dumps
from requests import put
from requests import delete


print(get('http://127.0.0.1:5000').text)

# B
address1 = 'http://' + input()
summ = 0
while data := int(get(address1).text):
    summ += data
print(summ)

# C
address2 = "http://" + input()
values: list[int | str] = get(address2).json()
print(sum(itm for itm in values if isinstance(itm, int)))

# D
address3 = 'http://' + input()
key = input()
data3 = get(address3).json()
print(data3.get(key, 'No data'))

# E
address4 = 'http://' + input()
ways = [i.strip() for i in stdin]
summ4 = 0
for way in ways:
    summ4 += sum(get(address4 + way).json())
print(summ4)

# F
# address = 'http://' + input() + '/users'
# data = get(address).json()
# names = []
# for i in data:
#     names.append(f"{i['last_name']} {i['first_name']}")
# for name in sorted(names):
#     print(name)


# G
# address = 'http://' + input() + '/users/' + input()
# d = ''.join(i for i in stdin)
# data = {}
# try:
#     data = get(address).json()
# except ValueError:
#     print('Пользователь не найден')
# if data:
#     for key in data:
#         d = d.replace('{' + key + '}', str(data[key]))
#     print(d)  
    
    
# H
address = 'http://' + input() + '/users'
data5 = {}
data5["username"] = input()
data5["last_name"] = input()
data5["first_name"] = input()
data5["email"] = input()
post(address, data5=dumps(data5))


# I
address = 'http://' + input() + '/users/' + input()
line = [i.strip().split('=') for i in stdin]
data6 = {}
for j in line:
    data6[j[0]] = j[1]
put(address, data=dumps(data6))


# J
address = 'http://' + input() + '/users/' + input()
delete(address)