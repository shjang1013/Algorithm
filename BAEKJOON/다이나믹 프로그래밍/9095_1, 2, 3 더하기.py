# 규칙
1 = (1)
2 = (1+1, 2)
3 = (1+1+1, 1+2, 2+1, 3)
4 = (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1)

# 나의 코드 
N = int(input())

dp = [1, 2, 4] + [0] * 7

for i in range(3, 10):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(N):
    print(dp[int(input())-1])

