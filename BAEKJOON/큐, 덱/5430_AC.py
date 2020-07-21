# 시간초과
import sys
from collections import deque

T = int(input())
for _ in range(T):
    # 큐의 상태
    flag = True
    
    # 수행할 함수
    p = input()
    
    # 배열에 들어있는 수의 개수
    n = int(input())
    
    # 문자열
    string = sys.stdin.readline().split()[0]
    
    # 배열
    queue = deque(list(map(int, string[1:len(string)-1].split(',')))) if n != 0 else []
    
    for i in p:
        if i == 'R':
            queue.reverse()
        else:
            if len(queue):
                queue.popleft()
            else:
                flag = False
                break

    # 출력값도 꼭 확인하기
    print(list(queue)) if flag else print("error")

# 수정한 코드
import sys
from collections import deque

T = int(input())
for _ in range(T):
    # 큐의 상태
    flag = True
    
    r_flag = True
    
    # 수행할 함수
    p = input()
    
    # 배열에 들어있는 수의 개수
    n = int(input())
    
    # 문자열
    string = sys.stdin.readline().split()[0]
    
    # 배열
    queue = deque(list(map(int, string[1:-1].split(',')))) if n != 0 else []
    
    for i in p:
        # 숫자의 순서 뒤집기
        if i == 'R':
            r_flag = not r_flag
        # 첫번째 숫자 버리기
        elif i == 'D' and queue:
            if r_flag:
                queue.popleft()
            else:
                queue.pop()
        # 큐가 비어있을 경우 & 수행할 함수 존재
        elif i == 'D' and not queue:
            flag = False
            break

    if not r_flag:
        queue.reverse()
    
    print('['+','.join(list(map(str, queue)))+']') if flag else print("error")

