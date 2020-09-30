# 직사각형을 채우는 방법의 수를 10007로 나눈 나머지를 출력하기
N = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3

for i in range(3, N+1):
    dp[i] = (2 * dp[i-2] + dp[i-1]) % 10007

print(dp[N])
