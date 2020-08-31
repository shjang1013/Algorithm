# 주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값을 출력하기
import sys

N = int(input())

coins = sorted(list(map(int, sys.stdin.readline().split())))

# 자연수
num = 1

for i in coins:
    if num < i:
        break
    num += i

print(num)
