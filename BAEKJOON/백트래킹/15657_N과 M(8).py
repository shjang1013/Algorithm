N, M = map(int, input().split())

List = sorted(list(map(int, input().split())))

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
        
        array[i] = List[j-1]
        for k in range(j):
            visited[k] = 1
        go(i + 1)
        for k in range(1, N + 1):
            visited[k] = 0

go(0)
