# 나의 코드
def solution(phone_number):
    # 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 '*'으로 가린 문자열을 리턴
    return (len(phone_number)-4)*'*' + phone_number[len(phone_number)-4:]


# 다른 코드(정규식) => TIL에 정리
import re

def solution(s):
    p = re.compile(r'\d(?=\d{4})')
    return p.sub("*", s, count = 0)

