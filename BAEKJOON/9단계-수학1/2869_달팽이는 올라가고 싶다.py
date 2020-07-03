# A : 낮에 올라가는 미터, B : 밤에 미끄러지는 미터, V : 최종 위치
# 시간초과
A, B, V = map(int, input().split())

height = day = 0

while True:
    day += 1
    height += A
    if height >= V:
        break
    height -= B

print(day)

# 다른 코드 참고
# 마지막에 올라갈 나무 막대를 제외하면 계산하기 좋음
A, B, V = map(int, input().split())

if (tree-A) % (A-B) == 0:
    print((tree-A) // (A-B) + 1)
else:
    print((tree-A) // (A-B) + 2)

# sys 이용, input() 보다 빠름 
import sys

A, B, tree = map(int, sys.stdin.readline().split())

if (tree-A) % (A-B) == 0:
    print((tree-A) // (A-B) + 1)
else:
    print((tree-A) // (A-B) + 2)

