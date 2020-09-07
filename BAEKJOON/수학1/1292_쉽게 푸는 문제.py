# 나의 코드
import sys

input = sys.stdin.readline

A, B = map(int, input().split())

A -= 1
N = 1
a = 1
a_ = False
b = 1
b_ = False

# 구간 끝의 모든 합 - 구간 처음의 모든 합
while True:
    if 2 * A < N * (N+1) and a_ == False:
        a = N
        a_ = True
    
    if 2 * B < N * (N+1) and b_ == False:
        b = N
        b_ = True
    
    if a_ and b_:
        break
    
    N += 1

sum_A = 0
for i in range(1, a):
    sum_A += i * i

sum_A += a * (A-((a-1)*a//2))

sum_B = 0
for i in range(1, b):
    sum_B += i * i

sum_B += b * (B-((b-1)*b//2))

print(sum_B-sum_A)


# 다른 코드 (구간의 끝이 1000이하이므로 미리 리스트 만들기)

List = []

for i in range(1, 46):
    List.append += [i] * i

A, B = map(int, input().split())
print(sum(List[A-1:B]))
