# 섬의 개수 구하기
import sys

# 재귀 최대 깊이 지정
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break

    array = [list(map(int, input().split())) for _ in range(h)]

    def DFS(x, y):
        if x <= -1 or x >= h or y <= -1 or y >= w:
            return False
        
        if array[x][y] == 1:
            array[x][y] = 0
            
            DFS(x-1, y-1)
            DFS(x-1, y)
            DFS(x-1, y+1)
            DFS(x, y-1)
            DFS(x, y+1)
            DFS(x+1, y-1)
            DFS(x+1, y)
            DFS(x+1, y+1)
            
            return True
        
        return False
    
    result = 0
    for i in range(h):
        for j in range(w):
            if DFS(i, j) == True:
                result += 1

    print(result)
