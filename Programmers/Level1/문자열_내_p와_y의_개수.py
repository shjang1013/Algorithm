# 나의 코드
def solution(s):
    p = 0
    y = 0
    for i in s:
        if i == 'p' or i == 'P':
            p += 1
        elif i == 'y' or i =='Y':
            y += 1

    if p == y:
        return True
    else:
        return False

# 다른 사람의 코드
def solution(s):
    
    # lower() : 소문자로 바꿔주는 메소드
    return s.lower().count('p') == s.lower().count('y')
