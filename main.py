from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from urllib import response
import requests
import os
a=input("请输入网址不加http")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}
url=("http://"+str(a))
r=requests.get(url,headers=headers)

#!/usr/bin/python

# -*- coding:utf-8 -*-

file = open('cookies.txt','a+')

file.write(str(r.cookies)+"\n")
input()
#a