# 문제
# SWEA 4869 - [파이썬 S/W 문제해결 기본 4일차] Stack1 - 종이붙이기

# 나의 코드
T = int(input())

memo = []

def rectangle(N):
    for i in range(N+1):
        if i >= 2:
            memo[i] = memo[i-1] + 2 * memo[i-2]
        
        # i가 0이거나 1일 경우
        else:
            memo[i] = 1

    return memo[N]

for tc in range(T):
    N = int(input())
    memo = [0] * (N+1)
    print('#%d %d' %(tc+1, rectangle(N//10)))

# 점화식 문제의 대부분은 마지막에 무엇이 오는지, 그것을 빼면 어떤 상태가 되는지 확인


