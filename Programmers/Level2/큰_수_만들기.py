# 나의 코드(시간 초과)
import itertools

def solution(number, k):
    answer = []
    for i in list(itertools.combinations(number, len(number) - k)):
        temp = ''
        for j in range(len(i)):
            temp += i[j]
        answer.append(int(temp))
    
    return str(max(answer))

# 수정한 코드
