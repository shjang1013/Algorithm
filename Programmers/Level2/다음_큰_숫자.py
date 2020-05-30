# 나의 코드
def solution(n):
    # 자연수 n이 주어졌을 때, n의 다음 큰 숫자를 리턴
    count = bin(n).count('1')
    m = n+1
    
    while True:
        if bin(m).count('1') == count:
            break
        m += 1
    
    return m

