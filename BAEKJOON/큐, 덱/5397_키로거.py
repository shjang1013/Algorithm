# 강산이의 비밀번호 출력하기 
# 커서의 위치 파악하기
from collections import deque

N = int(input())

for _ in range(N):
    l = deque()
    r = deque()
    password = input()
    
    for i in password:
        if i == '<':
            if l:
                r.appendleft(l.pop())
    
        elif i == '>':
            if r:
                l.append(r.popleft())

        elif i == '-':
            if l:
                l.pop()
        
        else:
            l.append(i)

    print(''.join(l) + ''.join(r))
