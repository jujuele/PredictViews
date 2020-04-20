import re
import locale
#locale.setlocale( locale.LC_ALL, 'en_US.UTF-8')

#crawler에서만 필요한 코드(년, 개월 단위 영상은 취급하지 않음)
def sub(keyword) :

    if '년' in keyword or '개월' in keyword:
        return -1

    else : return 1


# 조회수, 구독자는 int형으로 바꿔줌

def stoi(keyword) :
    keyword = keyword.replace(',','')

    if '만' in keyword:
        digit = re.findall("\d+", keyword)
        i = float(digit[0]) * 10000
        return i

    elif '천' in keyword:
        digit = re.findall("\d+", keyword)
        i = float(digit[0]) * 1000
        return i

    elif '개' in keyword or '회' in keyword:
        digit = re.findall("\d+", keyword)
        return digit

    else : return keyword

