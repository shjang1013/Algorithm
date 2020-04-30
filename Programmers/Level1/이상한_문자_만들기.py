# 나의 코드(오답)
def solution(s):
    # 공백이 여러 개 올 수 있음 => 그러나 split()을 이용하면 공백을 여러 개이더라도 한 개로 인식
    answer = list(s.split())
    for i in range(len(answer)):
        temp = ''
        for j in range(len(answer[i])):
            if j & 1:
                temp += answer[i][j].lower()
            else:
                temp += answer[i][j].upper()

    answer[i] = temp

    return ' '.join(answer)


# 다른 코드(오답)
def solution(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])


# 수정한 코드
def solution(s):
    answer = ''
    id = 0
    for i in s:
        # 알파벳
        if i.isalpha():
            if id & 1:
                answer += i.lower()
            else:
                answer += i.upper()
            id += 1
        # 공백
        else:
            id = 0
            answer += ' '

    return ''.join(answer)
