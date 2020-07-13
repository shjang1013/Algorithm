# 동적 계획법(다이나믹 프로그래밍)을 이용
# 4번째부터 규칙 존재
def triangle(N):
    f = [0, 1, 1, 1]
    
    for i in range(4, N+1):
        f.append(f[i-3]+f[i-2])
    
    return f[N]

T = int(input())

for _ in range(T):
    N = int(input())
    print(triangle(N))
