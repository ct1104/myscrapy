#!/usr/bin/env python3
import requests
from pyquery import PyQuery as pq

url='https://vpnso.com/account/ssh_list.php'
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','cookie':'PHPSESSID=value1; UserAutoLoginInfo=value2','referer':'https://vpnso.com/account/login.php?r=%2Faccount%2Fssh_list.php'}
r=requests.get('https://vpnso.com/account/ssh_detail.php?ID=22143',headers=headers)
doc=pq(r.text)
s=doc('select')
for sc in s('#iservers').children():
    print(sc.attrib['value'])
