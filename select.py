import re

# 오래된 동영상은 찾지 않음

def sub(keyword) :

    if '년' in keyword or '개월' in keyword:
        return -1

    else : return 1


# 조회수, 구독자는 int형으로 바꿔줌

def stoi(keyword) :
    if '만' in keyword:
        digit = re.findall("\d+", keyword)
        i = float(digit[0]) * 10000
        return i

    elif '천' in keyword:
        digit = re.findall("\d+", keyword)
        i = float(digit[0]) * 1000
        return i

    else : return keyword
