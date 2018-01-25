import requests
import re

PATTERN_DIV_RANK02 = re.compile(r'<div class="ellipsis rank02">.*?</div>', re.DOTALL)
PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')
PATTERN_IMG_ONERROR = re.compile(r'<img onerror.*?>')
PATTERN_SRC = re.compile(r'src="(.*?)"')
PATTERN_TD = re.compile(r'<td.*?>.*?</td?')
PATTERN_IMG = re.compile(r'<img.*?src="(.*?)".*?>', re.DOTALL)

response = requests.get('https://www.melon.com/chart/index.htm')
source = response.text

match_list1 = re.finditer(PATTERN_DIV_RANK02, source)
for match_div_rank02 in match_list1:
    # 각 순회에서 매치된 전체 문자열 (<div clas... ~ </div>)부분을 가져옴
    div_rank02_content = match_div_rank02.group()

    # 부분 문자열에서 a태그의 내용을 title변수에 할당
    match_title = re.search(PATTERN_A_CONTENT, div_rank02_content)
    title = match_title.group(1)
    print(title)

match_list2 = re.finditer(PATTERN_IMG_ONERROR, source)
for match_img_onerror in match_list2:
    # 각 순회에서 매치된 전체 문자열 (<div clas... ~ </div>)부분을 가져옴
    img_onerror_content = match_img_onerror.group()

    match_img_src = re.search(PATTERN_SRC, img_onerror_content)
    img = match_img_src.group(1)
    print(img)