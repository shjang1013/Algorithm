# 1부터 N까지 자연수 중에서 중복 포함 M개를 고른 수열
# 수열은 오름차순으로 출력해야 한다.
N, M = map(int, input().split())

visited = [0] * (N+1)
array = [0] * M


def go(i):
    if i == M:
        for j in range(M):
            print(array[j], end=' ')
        print()
        return

    for j in range(1, N + 1):
        if visited[j]:
            continue
        
        array[i] = j
        for k in range(j):
            visited[k] = 1
        go(i+1)
        for k in range(1, N+1):
            visited[k] = 0

go(0)
