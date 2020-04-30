# 나의 코드
def solution(n):
    answer = 0
    n = str(n)
    
    for i in n:
        answer += int(i)
    
    return answer


# 간단 버전 코드
def solution(n):
    return sum([int(i) for i in str(n)])
