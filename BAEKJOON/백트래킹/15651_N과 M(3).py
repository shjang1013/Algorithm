# 1부터 N까지 자연수 중에서 중복 포함 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
N, M = map(int, input().split())

array = [0] * M

def go(i):
    if i == M:
        for j in range(M):
            print(array[j], end=' ')
        print()
        return
    
    for j in range(1, N+1):
        array[i] = j
        go(i+1)

go(0)

