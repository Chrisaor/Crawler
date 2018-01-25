import re
import requests


response = requests.get('https://www.melon.com/chart/index.htm')
source = response.text

PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">(.*?)</div>', re.S)
PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')

match_list = re.finditer(PATTERN_DIV_RANK01, source)

title_list = list()
for match in match_list:
    result = re.search(PATTERN_A_CONTENT, match.group())
    title_list.append(result.group(1))
print(title_list)


#
# PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">(.*?)</div>', re.S)
# PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')
#
# match_list = PATTERN_DIV_RANK01.finditer(source)
#
# title_list = list()
# for i in match_list:
#     result = PATTERN_A_CONTENT.search(i.group())
#     title_list.append(result.group(1))
#     print(title_list)