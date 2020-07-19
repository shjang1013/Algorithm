# 정수를 저장하는 덱(Deque)을 구현
from collections import deque
import sys

Deque = deque([])

N = int(input())

for _ in range(N):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push_front':
        Deque.appendleft(command[1])
    elif command[0] == 'push_back':
        Deque.append(command[1])
    elif command[0] == 'pop_front':
        print(Deque.popleft()) if len(Deque) else print(-1)
    elif command[0] == 'pop_back':
        print(Deque.pop()) if len(Deque) else print(-1)
    elif command[0] == 'size':
        print(len(Deque))
    elif command[0] == 'empty':
        print(0) if len(Deque) else print(1)
    elif command[0] == 'front':
        print(Deque[0]) if len(Deque) else print(-1)
    elif command[0] == 'back':
        print(Deque[-1]) if len(Deque) else print(-1)
