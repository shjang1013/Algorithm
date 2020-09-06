# input() 사용할 경우 시간초과
import sys

input = sys.stdin.readline

from collections import deque

queue = deque()

N = int(input())

for _ in range(N):
    command = input().split()
    
    if command[0] == "push":
        queue.append(command[1])
    
    elif command[0] == "pop":
        print(queue.popleft()) if queue else print(-1)
    
    elif command[0] == "size":
        print(len(queue))
    
    elif command[0] == "empty":
        print(0) if queue else print(1)
    
    elif command[0] == "front":
        print(queue[0]) if queue else print(-1)
    
    elif command[0] == "back":
        print(queue[-1]) if queue else print(-1)
