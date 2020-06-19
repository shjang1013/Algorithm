# 나의 코드
def solution(s):
    answer = ''
    flag = True
    for i in s:
        # 공백문자 다음은 대문자 / flag 이용하기 
        if i == ' ':
            answer += ' '
            flag = True
        elif flag:
            answer += i.upper()
            flag = False
        else:
            answer += i.lower()

    return answer
