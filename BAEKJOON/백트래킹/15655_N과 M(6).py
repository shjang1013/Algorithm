# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 오름차순

N, M = map(int, input().split())

List = sorted(list(map(int, input().split())))

visited = [0] * (N + 1)

array = [0] * M

def go(i, start):
    if i == M:
        for j in range(M):
            print(array[j], end=' ')
        print()
        return

    for j in range(start, N + 1):
        if visited[j]:
            continue
        
        visited[j] = 1
        array[i] = List[j-1]
        go(i + 1, j + 1)
        visited[j] = 0

go(0, 1)
