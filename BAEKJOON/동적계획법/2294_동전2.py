# 입력받기
N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))

# DP 테이블 초기화
dp = [0] + [10001] * K

# 다이나믹 프로그래밍
for i in range(N):
    for j in range(coins[i], K+1):
        if dp[j-coins[i]] != 10001:
            dp[j] = min(dp[j], dp[j-coins[i]] + 1)

# 결과 출력 
if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])
