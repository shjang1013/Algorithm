# 이진 탐색을 이용한 부품 찾기
import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None


N = int(sys.stdin.readline().rstrip())

array = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())

x = list(map(int, sys.stdin.readline().split()))

array.sort()

for i in x:
    result = binary_search(array, i, 0, N-1)
    
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')


# 계수정렬(Count Sort)을 이용한 부품 찾기
N = int(input())

array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

M = int(sys.stdin.readline().rstrip())

x = list(map(int, sys.stdin.readline().split()))

for i in x:
    if array[i] == 1:
        print("yes", end=' ')
    else:
        print("no", end=' ')


# set() 함수를 이용한 부품 찾기
N = int(sys.stdin.readline().rstrip())

array = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())

x = list(map(int, sys.stdin.readline().split()))

for i in x:
    if i in array:
        print("yes", end=' ')
    else:
        print("no", end=' ')
