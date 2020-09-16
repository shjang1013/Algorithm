# 동적 계획법(다이나믹 프로그래밍)을 이용한 피보나치
# fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하기
import sys

def fibo(N):
    f = [(1, 0), (0, 1)]
    
    for i in range(2, N+1):
        f.append((f[i-2][0]+f[i-1][0], f[i-2][1]+f[i-1][1]))
    
    return f[N]

N = int(input())

for _ in range(N):
    T = fibo(int(sys.stdin.readline()))
    print(T[0], T[1])
