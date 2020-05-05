# 나의 코드
def solution(dartResult):
    # 다트 게임 : 부분 점수 계산 로직
    answer = []
    sdt = ['S', 'D', 'T']
    temp = ''
    for i in dartResult:
        if i.isdigit():
            temp += i
        elif i in sdt:
            answer.append(int(temp) ** (sdt.index(i)+1))
            temp = ''
        elif i == '*':
            answer[-1] *= 2
            if len(answer) != 1:
                answer[-2] *= 2
        elif i == '#':
            answer[-1] *= -1

    return sum(answer)

# 다른 코드
import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    
    answer = sum(dart)
    return answer
