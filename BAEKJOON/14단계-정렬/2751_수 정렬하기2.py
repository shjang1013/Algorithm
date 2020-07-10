# N개의 수가 주어졌을 때, 오름차순으로 정렬하기
# PyPy3로 채점하면 통과, Python3로 채점하면 시간초과
N = int(input())

# 입력받기
List = [int(input()) for _ in range(N)]

# 리스트 정렬하기
List.sort()

# 리스트 출력하기
for i in List:
    print(i)


# 숏코딩
for i in sorted([int(input()) for _ in range(int(input()))]):
    print(i)


# 수정한 코드
import sys

N = int(sys.stdin)

List = sorted([int(sys.stdin) for _ in range(N)])

for i in List:
    print(i)

# PyPy3 메모리 : 211060KB, 시간 : 860ms
# Python3 메모리 : 82224KB, 시간 : 1368ms
# 리스트의 정렬(sort) 대신 sort 종류 정리하기
