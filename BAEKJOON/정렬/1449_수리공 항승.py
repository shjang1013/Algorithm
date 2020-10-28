# 테이프의 개수 출력하기
N, L = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

count = 0

tape = 0

for i in array:
    if tape < i:
        count += 1
        tape = i + L - 1

print(count)
