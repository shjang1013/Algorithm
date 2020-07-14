# 동적 계획법(다이나믹 프로그래밍)을 이용
# N이 주어졌을 때 지원이가 만들 수 있는 모든 가짓수를 세는 것
def binary(N):
    f = [0, 1, 2]
    
    for i in range(3, N+1):
        f.append(f[i-2]%15746+f[i-1]%15746)
    
    return f[N]%15746

N = int(input())

print(binary(N))
