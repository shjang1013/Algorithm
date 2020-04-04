# 문제
# SWEA 5189 - [파이썬 S/W 문제해결 구현 2일차] 완전 검색 - 전자카트

# 수정한 코드(다른 코드 참고)
def DFS(S):
    global temp, num, result
    
    if len(temp) == N-1:
        for i, j in temp:
            num += Battery[i][j]
        
        num += Battery[S][0]
        result.append(num)
        num = 0
        return
    
    for i in range(1, N):
        if not visited[i]:
            temp.append((S, i))
            visited[i] = True
            DFS(i)
            temp.remove((S, i))
            visited[i] = False


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Battery = [list(map(int, input().split())) for _ in range(N)]
    
    visited = [0] * N
    num = 0
    temp =  []
    result =[]
    
    DFS(0)
    
    print('#%d %d'%(tc, min(result)))
