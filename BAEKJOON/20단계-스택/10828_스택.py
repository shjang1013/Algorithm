import sys

N = int(input())

stack = []

for _ in range(N):
    # command를 input()을 이용하여 받을 경우 시간초과
    command = sys.stdin.readline().split()
    
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == 'pop':
        print(stack.pop()) if len(stack) else print("-1")
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print("0") if len(stack) else print("1")
    else:
        print(stack[-1]) if len(stack) else print("-1")
