import requests
from bs4 import BeautifulSoup

header_into = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
        'Host':'www.zhihu.com',
        'Connection': 'keep-alive',
        'Referer': 'http://www.zhihu.com/'
        }
login_data = {
        'email':'931208707@qq.com',
        'password':'*****',
        'rememberme':'true',
        }

#This is email-account login page
url = 'http://www.zhihu.com/login/email'
s = requests.Session()
r = s.post(url,data=login_data,headers=header_into)
print r.status_code

#Now you can skip and analysis page
soup = BeautifulSoup(s.get('http://www.zhihu.com/question/29925879').content,"lxml")
