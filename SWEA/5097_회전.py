# 문제
# SWEA 5097 - [파이썬 S/W 문제해결 기본 6일차] Queue - 회전

# 나의 코드

# N개의 숫자로 이루어진 수열이 주어진다. 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자를 출력하는 프로그램

# N의 배수만큼 맨 앞의 숫자를 맨 뒤로 보내는 작업을 했을 경우, 처음 주어지는 수열과 같다.
# 따라서 M을 N으로 나눈 나머지만큼 맨 앞의 숫자를 맨 뒤로 보내는 작업을 실행하면 된다.

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    
    remainer = M % N
    
    for _ in range(remainer):
        queue.append(queue.pop(0))
    
    print("#%d %d" %(tc+1, queue[0]))


