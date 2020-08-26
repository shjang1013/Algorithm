# 배열 A에서 3번째 큰 값을 출력
import sys
T = int(input())

for _ in range(T):
    List = sorted(list(map(int, sys.stdin.readline().split())))
    print(List[-3])
