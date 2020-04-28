# 나의 코드
def solution(n):
    answer = '수박'
    
    if n & 1:
        answer = answer * (n//2) + '수'
    else:
        answer = answer * (n//2)
    
    return answer

# 다른 코드
def solution(n):
    answer = '수박' * n
    return answer[:n]
