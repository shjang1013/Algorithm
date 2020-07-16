# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
# [1,2,3,4,5,6,7,8] => [4,3,6,8,7,5,2,1]
import sys

N = int(input())

stack = []
op = []
count = 1
temp = True
for i in range(N):
    n = int(sys.stdin.readline())
    
    while count <= n:
        stack.append(count)
        op.append("+")
        count += 1
    
    if stack[-1] == n:
        stack.pop()
        op.append("-")
    else:
        temp = False
        break

if temp == False:
    print("NO")
else:
    print('\n'.join(op))
