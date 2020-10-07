# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 
N, M = map(int, input().split())

List = sorted(list(map(int, input().split())))

visited = [0] * N
array = [0] * M

def go(i):
    if i == M:
        for j in range(M):
            print(array[j], end=' ')
        print()
        return

    for j in range(N):
        if visited[j]:
            continue
        
        visited[j] = 1
        array[i] = List[j]
        go(i+1)
        visited[j] = 0

go(0)
