# 나의 코드
def solution(n):
    answer = [0]
    for i in range(n-1):
        temp = answer
        answer = answer + [0]
        for j in range(len(temp)):
            if temp[i] & 1:
                temp[i] = 0
            else:
                temp[i] = 1
        answer = answer + temp
    
    return answer


