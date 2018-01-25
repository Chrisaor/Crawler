import re

# Patterns
# <div class="ellipsis rank01> ~ </div>부분의 텍스트
PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
# <a href=....>(내용)</a>
PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')

save()
# 로컬 HTML문서 불러오기
source = open('melon.html', 'rt').read()

# 전체 문서에서 PATTERN_DIV_RANK01에 해당하는 match object목록을 순회
match_list = re.finditer(PATTERN_DIV_RANK01, source)
for match_div_rank01 in match_list:
    # 각 순회에서 매치된 전체 문자열 (<div clas... ~ </div>)부분을 가져옴
    div_rank01_content = match_div_rank01.group()

    # 부분 문자열에서 a태그의 내용을 title변수에 할당
    match_title = re.search(PATTERN_A_CONTENT, div_rank01_content)
    title = match_title.group(1)
    print(title)