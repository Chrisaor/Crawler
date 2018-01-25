import requests
import re

response = requests.get("https://www.melon.com/chart/index.htm")
source = response.text

def get_tag_attribute(attribute_name, tag_string):
    if attribute_name == 'type':
        result = re.findall(r'type="(.*?)"', tag_string)
    elif attribute_name == 'title':
        result = re.findall(r'title="(.*?)"', tag_string)
    elif attribute_name == 'class':
        result = re.findall(r'class="(.*?)"', tag_string)
    elif attribute_name == 'onClick':
        result = re.findall(r'onClick="(.*?)"', tag_string)
    return result


string = '''<button type="button" title="뮤직비디오" class="button_icsource = '<div><span class="abc">ASDF</span></div>'ons video "  onClick="melon.link.goMvDetail('19030101', '30784303','song');">'''
print(get_tag_attribute('type', string))
print(get_tag_attribute('title', string))
print(get_tag_attribute('class', string))
print(get_tag_attribute('onClick', string))
# with open('melon.html', 'rt') as f:
#     source = f.read()

PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">(.*?)</div>', re.S)
PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')

match_list = PATTERN_DIV_RANK01.finditer(source)

title_list = list()
for i in match_list:
    result = PATTERN_A_CONTENT.search(i.group())
    title_list.append(result.group(1))
    # print(title_list)
    # break;


PATTERN_DIV_RANK02 = re.compile(r'<div class="ellipsis rank02">(.*?)</div>', re.S)
found_list = PATTERN_DIV_RANK02.finditer(source)

artist_list = list()
for i in found_list:
    result = PATTERN_A_CONTENT.search(i.group())
    artist_list.append(result.group(1))
# print(artist_list)

PATTERN_DIV_RANK03 = re.compile(r'<div class="ellipsis rank03">(.*?)</div>', re.S)
rank3_list = PATTERN_DIV_RANK03.finditer(source)

album_list = list()
for i in rank3_list:
    result = PATTERN_A_CONTENT.search(i.group())
    album_list.append(result.group(1))
# print(album_list)

melon_chart = dict()

result_list = list(zip(range(1,101), title_list, artist_list, album_list))


final_list = list()
for i in result_list:
    result_dict = dict()
    result_dict["rank"] = i[0]
    result_dict["title"] = i[1]
    result_dict["artist"] = i[2]
    result_dict["album"] = i[3]
    final_list.append(result_dict)

#
# for i in final_list:
#     print(i)
