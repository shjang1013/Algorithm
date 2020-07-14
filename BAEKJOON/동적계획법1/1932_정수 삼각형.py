# 동적 계획법(다이나믹 프로그래밍)을 이용
import sys

def triangle(N, tri):
    for i in range(len(tri[1])):
        tri[1][i] += tri[0][0]
    
    # 위에서부터 최댓값 더하기
    for i in range(2, N):
        for j in range(len(tri[i])):
            if j == 0:
                tri[i][j] += tri[i - 1][j]
            elif j == len(tri[i])-1:
                tri[i][j] += tri[i - 1][j - 1]
            else:
                tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

    return max(tri[N-1])

N = int(input())
tri = []

for _ in range(N):
    tri.append(list(map(int, sys.stdin.readline().split())))

print(triangle(N, tri))
