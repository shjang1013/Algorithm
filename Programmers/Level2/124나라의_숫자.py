# 나의 코드
def solution(n):
    # 3진법을 이용, 나머지가 0인 경우 몫에서 1을 빼줘야 한다.
    answer = ''
    
    while n:
        n, nam = divmod(n, 3)
        answer = "412"[nam] + answer
        
        if not nam:
            n -= 1
    return answer

# 다른 코드
def solution(n):
    num = ['1','2','4']
    answer = ""
    
    
    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3
    
    return answer
