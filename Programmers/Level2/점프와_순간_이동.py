# 나의 코드
def solution(n):
    # 순간이동 : 1, 2, 4, 8, 16, 32, ...
    # 홀수일 경우 1을 빼고 2로 나눌 것
    answer = 0
    
    while n != 0:
        if n & 1:
            n = n - 1
            answer += 1 # 건전지 사용량 
        n //= 2

    return answer
