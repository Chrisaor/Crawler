import re
import requests

response = requests.get('https://www.melon.com/chart/index.htm')
source = response.text

DIV_RANK01 = re.compile(r'<div class="ellipsis rank01>.*?</div>', re.DOTALL)
A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')

for i in re.finditer(DIV_RANK01, source):
    print(i)