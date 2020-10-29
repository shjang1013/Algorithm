# 수열 array의 가장 긴 증가하는 부분 수열의 길이를 출력하기
N = int(input())

array = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
