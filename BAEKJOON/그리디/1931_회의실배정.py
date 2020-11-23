# (끝나는 시간 순, 시작하는 시간 순)으로 정렬하여 회의의 최대 개수 카운트하기
import sys
input = sys.stdin.readline

N = int(input())

array = []

for _ in range(N):
    s, e = map(int, input().split())
    array.append((s, e))

array.sort(key=lambda x:(x[1], x[0]))

start, count = 0, 0

for i in array:
    if start <= i[0]:
        start = i[1]
        count += 1

print(count)
