# 문제
# SWEA 4828 - [파이썬 S/W 문제해결 기본 1일차] LIST1 - minmax

num = int(input())

for i in range(1, num+1):
    test_num = int(input())
    test_case = list(map(int, input().split()))
    print('#{0} {1}' .format(i, max(test_case)-min(test_case)))
