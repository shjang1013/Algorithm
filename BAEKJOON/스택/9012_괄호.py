# input()는 시간초과 발생할 수도 있음 => sys.stdin.readline() 사용
import sys

T = int(input())

for _ in range(T):
    # sys.stdin.readline()은 개행을 포함하기 때문에 strip() 사용할 것
    bracket = sys.stdin.readline().strip()
    stack = []
    for i in bracket:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                stack.append(i)
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                break

    print("NO") if len(stack) != 0 else print("YES")

# 다른 풀이(replace 이용)
import sys

T = int(input())

for _ in range(T):
    bracket = sys.stdin.readline().strip()
    
    for i in range(len(bracket)):
        bracket = bracket.replace('()', '')
    
    if bracket == '':
        print("YES")
    else:
        print("NO")
