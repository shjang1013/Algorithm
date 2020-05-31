# 나의 코드 ( 런타임에러 & 시간초과 )
def Fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)

def solution(n):
    return Fibo(n) % 1234567


# 수정한 코드
def solution(n):
    answer = 0
    i, j = 0, 1
    for _ in range(2, n+1):
        i, j = j, i + j

    return j % 1234567
