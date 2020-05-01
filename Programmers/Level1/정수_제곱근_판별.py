# 나의 코드
def solution(n):
    k = 1
    answer = 0
    while k * k < n:
        k += 1
    if k * k == n:
        answer = (k+1)*(k+1)
    else:
        answer = -1
    return answer

# 다른 사람의 코드
def solution(n):
    sqrt = n** (1/2)
    
    if sqrt % 1 == 0: # sqrt이 양의 정수라면
        return (sqrt + 1) ** 2
    return -1

# 또 다른 코드
from math import sqrt

def solution(n):
    return -1 if sqrt(n) % 1 else (sqrt(n)+1)**2
