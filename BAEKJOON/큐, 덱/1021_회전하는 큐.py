# N개의 원소를 포함하고 있는 양방향 순환 큐, 큐에서 원소 뽑기
from collections import deque
import sys

N, M = map(int, input().split())
List = list(map(int, sys.stdin.readline().split()))
queue = deque([i for i in range(1, N + 1)])
sum = 0

for i in List:
    if i == queue[0]:
        queue.popleft()
        continue
    
    # 2번, 3번 연산의 최솟값 출력
    left = queue.index(i)
    right = len(queue) - left

    if left <= right:
        queue.rotate(-left)
        queue.popleft()
        sum += left
    else:
        queue.rotate(right)
        queue.popleft()
        sum += right

print(sum)
