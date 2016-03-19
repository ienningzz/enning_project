#encoding=utf-8
import requests
from bs4 import BeautifulSoup

url = 'http://www.chsi.com.cn/cet/query'
data = {
        'zkzh':'360012152114411',
        'xm': '黄康德'
        }
headers = {
        'User-Algent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
        'Referer':'http://www.chsi.com.cn/cet/'
        }
r = requests.get(url,params=data,headers=headers)
print BeautifulSoup(r.content,'lxml').find('table',class_='cetTable').getText()
