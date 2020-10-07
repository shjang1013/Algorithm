# 시간초과
import sys
input = sys.stdin.readline

editor = list(input().rstrip())

N = int(input())

l = len(editor)

cursor = l

for _ in range(N):
    command = input().split()
    
    if command[0] == 'L':
        if cursor != 0:
            cursor -= 1

elif command[0] == 'D':
    if cursor != l:
        cursor += 1
    
    elif command[0] == 'B':
        if cursor != 0:
            del editor[cursor-1]
            cursor -= 1

elif command[0] == 'P':
    editor.insert(cursor, command[1])
    cursor += 1

print(''.join(editor))

# 수정한 코드(deque 이용)
import sys
from collections import deque

input = sys.stdin.readline

editor = deque(input().rstrip())

N = int(input())

l = len(editor)

stack = deque()

for _ in range(N):
    command = input().split()
    
    if command[0] == 'L':
        if editor:
            stack.appendleft(editor.pop())

    elif command[0] == 'D':
        if stack:
            editor.append(stack.popleft())
    
    elif command[0] == 'B':
        if editor:
            editor.pop()

    elif command[0] == 'P':
        editor.append(command[1])

print(''.join(editor)+''.join(stack))
