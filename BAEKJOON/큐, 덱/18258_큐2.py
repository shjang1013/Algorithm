# queue.pop(0)에서 시간초과
import sys

N = int(input())

queue = []

for _ in range(N):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        print(queue.pop(0)) if len(queue) else print("-1")
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == 'empty':
        print("0") if len(queue) else print("1")
    elif command[0] == 'front':
        print(queue[0]) if len(queue) else print("-1")
    elif command[0] == 'back':
        print(queue[-1]) if len(queue) else print("-1")


# 수정한 코드
import sys

from collections import deque

N = int(input())

queue = deque([])

for _ in range(N):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        print(queue.popleft()) if len(queue) else print("-1")
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == 'empty':
        print("0") if len(queue) else print("1")
    elif command[0] == 'front':
        print(queue[0]) if len(queue) else print("-1")
    elif command[0] == 'back':
        print(queue[-1]) if len(queue) else print("-1")
