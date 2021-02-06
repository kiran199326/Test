import requests as req
import requests.exceptions
import re
import urllib3
import threading
import time
from bs4 import BeautifulSoup
import os
import sys

start = time.time()
try:
    os.remove("xtor.txt")
except FileNotFoundError:
    pass
content = ''
s = req.session()
s.cookies.clear()
s.cookies.keys()
u = []
for i in range(1, 150): u.append("https://1337x.unblockit.ltd/cat/Other/" + str(i))


def fetch_url(url):
    global content
    global resp12
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
    try:
        resp12 = req.get(url, headers=headers, timeout=20)
    except requests.exceptions.ReadTimeout:
        pass
    except requests.exceptions.ConnectionError:
        pass
    res1 = resp12.text
    #    print(res1)
    content = content + '\n' + res1


threads = [threading.Thread(target=fetch_url, args=(url,)) for url in u]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

cleantext = BeautifulSoup(content, "lxml").text
with open('xtor.txt', 'a+', encoding="utf-8")as f:
    for line in cleantext.split('\n'):
        if line: f.write(line + '\n')
f.close()
#os.remove("xtor1.txt")


def line_del():
    flag = 1
    linelist1 = open("xtor1.txt", 'a+', encoding="utf-8")
    with open('xtor.txt', 'r', encoding="utf-8")as f:
        for line in f.readlines():
            if line.startswith("Download Tutorials Other Torrents - xtor Torrents") or " << " in line:
                flag = 0
            if line.startswith("leech") or line.startswith("xtor Torrents"):
                flag = 1
            if line and flag and not line.startswith("leech") and not line.startswith("xtor Torrents"):
                linelist1.write(line)
    f.close()
    linelist1.close()


line_del()
for x in u:
    print(x)
print("Elapsed Time: %s", (time.time() - start))
