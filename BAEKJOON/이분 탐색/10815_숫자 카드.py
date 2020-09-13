# 재귀함수를 이용한 이진 탐색
def binary_search(array, target, start, end):
    if start > end:
        return False
    
    mid = (start+end) // 2
    
    if array[mid] == target:
        return True
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    
    else:
        return binary_search(array, target, mid+1, end)

N = int(input())

A = list(map(int, input().split()))

# 정렬된 리스트
A.sort()

M = int(input())

array = list(map(int, input().split()))

for i in range(M):
    result = binary_search(A, array[i], 0, N-1)
    
    if result == False:
        print(0, end=' ')
    else:
        print(1, end=' ')

