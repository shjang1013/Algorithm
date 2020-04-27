def solution(s):
    answer = ''
    
    # s의 길이
    n = len(s)
    
    # 홀수
    if len(s) & 1:
        answer = s[n//2]
    # 짝수
    else:
        answer = s[n//2-1:n//2+1]
    
    return answer
