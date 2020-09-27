# 상근이가 먹을 수 있는 사탕의 최대 개수 구하기 
import sys
input = sys.stdin.readline

N = int(input())

candy = [list(input().rstrip()) for _ in range(N)]

MAX = 0

def check():
    global MAX
    
    # 가로
    for i in range(N):
        a = 1
        for j in range(N-1):
            if candy[i][j] == candy[i][j+1]:
                a += 1
            else:
                if MAX < a:
                    MAX = a
                a = 1
    
        if MAX < a:
            MAX = a

    # 세로
    for i in range(N):
        a = 1
        for j in range(N - 1):
            if candy[j][i] == candy[j+1][i]:
                a += 1
            else:
                if MAX < a:
                    MAX = a
                a = 1

        if MAX < a:
                MAX = a

for i in range(N):
    for j in range(N-1):
        # 가로
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        check()
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        
        # 세로
        candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
        check()
        candy[j][i], candy[j + 1][i] = candy[j + 1][i], candy[j][i]

print(MAX)
