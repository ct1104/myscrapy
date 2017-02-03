#!/usr/bin/env python
import pprint
import urllib2
import cookielib
import requests
from pyquery import PyQuery as pq

cookie=''
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

LOGIN_URL='https://vpnso.com/account/login.php'
r=urllib2.urlopen(LOGIN_URL)
#pprint.pprint(cj._cookies.values())
for c in cj:
    cookie+=c.name+'='+c.value+';'
print cookie  #print cookies
cookies={}
cookies['PHPSESSID']=cookie[10:-1]

FORM_DATA={'rurl':'','user_pass':'loginpassword','user_email':'login_email','remember':''}
DO_LOGIN_URL='https://vpnso.com/account/do.php?action=login' #click 'login' button will visit this url
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
r=requests.request('POST',DO_LOGIN_URL,headers=headers,data=FORM_DATA,cookies=cookies) #login need cookies(dict format)
#print r.headers
DEST_URL='https://vpnso.com/account/ssh_detail.php?ID=22143'
request_headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','referer':'https://vpnso.com/account/ssh_list.php','cookie':cookie,'authority':'vpnso.com','path':'/account/ssh_detail.php?ID=22143'}
r=requests.request('GET',DEST_URL,headers=request_headers)
#print r.text
#extract proxy servers
doc=pq(r.text)
s=doc('select')
for sc in s('#iservers').children():
    print(sc.attrib['value'])


