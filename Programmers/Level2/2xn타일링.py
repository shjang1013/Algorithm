# 나의 코드
def rectangle(n):
    nemo = [0] * (n+1)
    for i in range(n+1):
        if i >= 2:
            nemo[i] = nemo[i-1] % 1000000007 + nemo[i-2] % 1000000007
        else:
            nemo[i] = 1
    return nemo[n]

def solution(n):
    return rectangle(n) % 1000000007


1. 이 문제에서 주의해야 할 점은 1000000007을 마지막에만 나눠주는 것이 아니라 계산값 내에서도 계속 나눠주어야 한다.
2. SWEA 4869 종이붙이기 문제와 유사하다.

