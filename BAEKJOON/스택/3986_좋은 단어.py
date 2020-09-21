from collections import deque
import sys

N = int(input())
count = 0
for _ in range(N):
    stack = deque([])
    s = sys.stdin.readline().rstrip()
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        count += 1

print(count)
