import requests

url = "https://1337x.unblockit.ltd/cat/Other/149/"

#payload={'test': 'txt'}
headers = {
  'Host': '1337x.unblockit.ltd',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'DNT': '1',
  'Connection': 'keep-alive',
  'Cookie': '__cfduid=dddcc3d3dcae83d88866060006eb6ac761612639302; __cfduid=d831df1b6fe014f346003c322b05cb3c81612635877; __cf_bm=ce92326c4d525401f8501f3098a17440dddba263-1612640200-1800-AXbfbpNstxzI2FeKsmE+2v/IQ2SoLDmViAjfFJFguMJHKeGX6770p5t2d196o4mv34w/x3QdNa6vu969vvqEqSY=',
  'Upgrade-Insecure-Requests': '1'
}

response = requests.request("GET", url, headers=headers, data={})

print(response.text)