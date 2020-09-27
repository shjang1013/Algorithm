# 직사각형을 채우는 방법의 수를 10007로 나눈 나머지를 출력하기

# 나의 코드
N = int(input())

dp = [1, 2] + [0] * 998

for i in range(2, 1000):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N-1]%10007)
