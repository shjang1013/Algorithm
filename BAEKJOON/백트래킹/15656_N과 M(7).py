N, M = map(int, input().split())

List = sorted(list(map(int, input().split())))

array = [0] * M

def go(i):
    if i == M:
        for j in range(M):
            print(array[j], end=' ')
        print()
        return

    for j in range(1, N+1):
        array[i] = List[j-1]
        
        go(i+1)

go(0)
