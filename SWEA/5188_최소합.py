# 문제
# SWEA 5188 - [파이썬 S/W 문제해결 구현 2일차] 완전 검색 - 최소합

# 수정한 코드(다른 코드 참고)
dy = [0, 1]
dx = [1, 0]

def Available(y,x):
    return 0<=y<N and 0<=x<N

def DFS(y,x):
    global temp, result
    
    # 최소값 구하기
    if result < temp:
        return
    
    # 오른쪽 아래까지 이동
    if y == N-1 and x == N-1:
        result = temp
        return
    
    # 오른쪽, 아래쪽으로만 이동 가능
    for i in range(2):
        newY = y + dy[i]
        newX = x + dx[i]
        
        if Available(newY, newX) and (newY, newX) not in visited:
            visited.append((newY, newX))
            temp += table[newY][newX]
            DFS(newY, newX)
            visited.remove((newY, newX))
            temp -= table[newY][newX]


T = int(input())
for tc in range(T):
    N = int(input())
    # 이차원 배열 받기 
    table = [list(map(int, input().split())) for _ in range(N)]
    
    visited = []
    
    temp, result = table[0][0], 10000
    DFS(0,0)
    print('#%d %d' %(tc+1, result))
