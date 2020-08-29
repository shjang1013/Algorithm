# 동적 계획법(다이나믹 프로그래밍)을 이용한 피보나치
def fibo(N):
    f = [0, 1]
    for i in range(2, N+1):
        f.append(f[i-2]+f[i-1])
    return f[N]

N = int(input())
print(fibo(N))
