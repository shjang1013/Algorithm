# 중복 빼고 오름차순으로 정렬하기
import sys

N = int(input())

List = sorted(list(set(map(int, sys.stdin.readline().split()))))

for i in List:
    print(i, end=' ')
