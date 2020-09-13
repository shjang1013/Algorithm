# 시간초과
# 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지 출력하기
def binary_search(array, target, start, end):
    if start > end:
        return False
    
    mid = (start+end) // 2
    
    if array[mid] == target:
        dict[array[mid]] += 1

    binary_search(array, target, start, mid - 1)
    binary_search(array, target, mid + 1, end)

    return True

N = int(input())

A = list(map(int, input().split()))

A.sort()

M = int(input())

array = list(map(int, input().split()))

dict = {}

for i in array:
    dict[i] = 0

for i in range(M):
    result = binary_search(A, array[i], 0, N-1)
    
    if result == False:
        print(0, end=' ')
    else:
        print(dict[array[i]], end=' ')
