import requests as req
import requests.exceptions
import re
import urllib3
from bs4 import BeautifulSoup
f =open('kickass.txt', 'w')
f.write("welcome\n")
f.close()
#resp = req.get("https://katcr.to/other/tutorials/?sortby=seeders&sort=desc")
content = ''
for i in range(1,20):
    ur= "https://katcr.to/other/tutorials/"+str(i)+"/?sortby=seeders&sort=desc"
    try:
        resp12=req.get(ur, timeout=5)
    except ConnectionError:
        print(ur+' Network connection failed.')
        resp12= None
        pass
    except Timeout:
        exit_after_echo(ur+' timeout.')
        resp12= None
        pass
    if resp12:
        resp1=resp12.text
        content = content + "\n" + resp1
cleantext = BeautifulSoup(content, "lxml").text
#f = open('kickass.txt' , 'a+')
with open('kickass.txt','a+',encoding="utf-8")as f:
    for line in cleantext.split('\n'):
        if line:f.write(line+'\n')
f.close()
