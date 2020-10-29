# 연속합 출력하기 
import sys
input = sys.stdin.readline

N = int(input())

array = list(map(int, input().split()))

dp = [0] * N

dp[0] = array[0]

for i in range(1, N):
    dp[i] = max(dp[i-1]+array[i], array[i])

print(max(dp))
