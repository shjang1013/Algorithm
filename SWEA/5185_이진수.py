# 문제
# SWEA 5185 - [파이썬 S/W 문제해결 구현 1일차] 시작하기 - 이진수

# 나의 코드
T = int(input())

for tc in range(T):
    N, List = input().split()
    List = format(int(List, 16), 'b')
    print('#%d %s' % (tc + 1, '0'+List))
