# 탑들의 순서대로 탑들에서 발사한 레이저 신호를 수신한 탑들의 번호를 출력하기
import sys
input = sys.stdin.readline

N = int(input())

array = list(map(int, input().split()))
stack = []
answer = [0] * N

for i in range(N):
    t = array[i]
    
    while stack and array[stack[-1]] < t:
        stack.pop()
    if stack:
        answer[i] = stack[-1] + 1
    
    stack.append(i)

print(' '.join(map(str, answer)))
