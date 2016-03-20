# -*- coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
from PIL import Image
import pytesseract

req = 'http://opac.ncu.edu.cn/reader/login.php'
vcode_path = 'http://opac.ncu.edu.cn/reader/captcha.php'
headers = {
        'Host':'opac.ncu.edu.cn',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
        'Connection': 'keep-alive',}
def down_png(sessi, img_path):
    with open('check.png','wb') as f:
        img_stream = sessi.get(img_path, stream=True)
        for chunk in img_stream.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()

def login(sessi,req,vcode,headers):
    data = {
            'number':'6****',
            'passwd':'******',
            'captcha':vcode,
            'select':'cert_no',
            'returnUrl': ''
            }
    r2 = sessi.post(req,data=data,headers=headers)
    print r2.status_code
    if r2.status_code == 200:
        print '[*] login seccess!' + r2.content
        print 
        return True
    else:
        return False

def get_vcode(sessi,vcode_path):
    vcode = ''
    while True:
        if re.match('\d{4}', vcode) is None:
            down_png(sessi, vcode_path)
            im = Image.open('check.png')
            vcode = pytesseract.image_to_string(im)
            vcode = vcode[:4]
        else:
            print 'verification code is ' + vcode
            break
    return vcode
sessi = requests.Session()
vcode = get_vcode(sessi, vcode_path)

if login(sessi,req,vcode,headers):
    print 'You successly log in'
else:
    print 'Please try again!'
