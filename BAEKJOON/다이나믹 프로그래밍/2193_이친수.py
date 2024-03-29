# N자리 이친수의 개수를 출력하기
N = 1 - 1
N = 2 - 10
N = 3 - 100, 101
N = 4 - 1000, 1001, 1010
N = 5 - 10000, 10001, 10010, 10100, 10101

# 나의 코드
N = int(input())

dp = [0] * 91

dp[1] = 1
dp[2] = 1

for i in range(3, N+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[N])
