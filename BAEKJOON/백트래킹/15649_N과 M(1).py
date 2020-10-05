# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 
N, M = map(int, input().split())

visited = [0] * (N+1)

array = [0] * M

def go(i):
    if i == M:
        for j in range(M):
            print(array[j], end=' ')
        print()
        return

    for j in range(1, N+1):
        if visited[j]:
            continue
        
        visited[j] = True
        array[i] = j
        go(i+1)
        visited[j] = False

go(0)
