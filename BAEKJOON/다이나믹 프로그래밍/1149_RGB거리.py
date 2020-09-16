# 동적 계획법(다이나믹 프로그래밍)을 이용
import sys

def RGB(N, cost, temp) :
    temp[0][0], temp[0][1], temp[0][2] = cost[0][0], cost[0][1], cost[0][2]
    
    # i번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 함
    for i in range(1, N):
        temp[i][0] = cost[i][0] + min(temp[i-1][1], temp[i-1][2])
        temp[i][1] = cost[i][1] + min(temp[i-1][0], temp[i-1][2])
        temp[i][2] = cost[i][2] + min(temp[i-1][0], temp[i-1][1])
    
    # 최솟값 반환
    MIN = min(dp[N-1][0], dp[N-1][1], dp[N-1][2])
    return MIN


N = int(input())
cost = []

for _ in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))

dp = [[0]*3 for _ in range(N)]

print(RGB(N, cost, dp))
