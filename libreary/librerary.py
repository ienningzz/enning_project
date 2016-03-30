# -*- coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
from PIL import Image
import pytesseract

vcode_path = 'http://opac.ncu.edu.cn/reader/captcha.php'
url = 'http://210.35.251.243/reader/redr_verify.php'
headers = {
        'Host':'opac.ncu.edu.cn',
        'Content-Type': 'application/x-www-form-urlencoded',
       'Referer':'http://lib.ncu.edu.cn/reader/redr_verify.php',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
        'Connection': 'keep-alive',
        'Content-Type':'application/x-www-form-urlencoded'
        }
user = '********'
password = '******'
def down_png(req, img_path,c):
    with open('check.png','wb') as f:
        img_stream = req.get(img_path,cookies=c, stream=True)
        for chunk in img_stream.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()

def login(req,user,vcode,password,headers,c):
    # datas = {'number':'*******',
    #        'passwd':'*******',
    #        'select':'cert_no',
    #        'returnUrl':''}
    data='number=********&passwd=*******&captcha={}&select=cert_no&returnUrl='.format(str(vcode))
#post is not json so use dictory;
    r2 = req.post(url,cookies=c,data=data,headers=headers,allow_redirects=True)
    print r2.status_code
    if r2.status_code == 200:
        print '[*] login seccess!' + r2.content
        print 
        return True
    else:
        return False

def get_vcode(req,vcode_path,c):
    vcode = ''
    while True:
        if re.match('\d{4}', vcode) is None:
            down_png(req, vcode_path,c)
            im = Image.open('check.png')
            vcode = pytesseract.image_to_string(im)
            vcode = vcode[:4]
        else:
            print 'verification code is ' + vcode
            break
    return vcode
req = requests.Session()
req.get('http://210.35.251.243/reader/login.php')
#cookies can make you save sessionID when you visit captcha page! 
c = req.cookies.get_dict()
vcode = get_vcode(req, vcode_path,c)

if login(req,user,vcode,password,headers,c):
    r = req.get('http://opac.ncu.edu.cn/reader/redr_info.php',cookies=c)
    soup = BeautifulSoup(r.content,"lxml")
    print soup.find_all(id="mylib_info")[0]
    print 'You successly log in'
