# 요세푸스 순열 출력하기
from collections import deque

N, K = map(int, input().split())

queue = deque([i for i in range(1, N+1)])

List = []

while queue:
    queue.rotate(-K)
    List.append(queue.pop())

# 출력
print('<', end = '')

for i in List[:N-1]:
    print(i, end=', ')

print(str(List[N-1]) + '>')
