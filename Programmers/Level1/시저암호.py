# 나의 코드
def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            # 시저 암호 : 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식
            temp = chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        elif i.islower():
            temp = chr((ord(i) - ord('a') +  n) % 26 + ord('a'))
        else:
            temp = ' '
        answer += temp
    
    return answer

# 다른 사람의 코드
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') +  n) % 26 + ord('a'))

    return ''.join(s)
