def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a
    
    # 두 정수 사이의 합 
    for i in range(a,b+1):
        answer += i
    
    return answer
