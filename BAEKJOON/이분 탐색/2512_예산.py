import sys
input = sys.stdin.readline

N = int(input())

array = list(map(int, input().split()))

M = int(input())

# 이진 탐색을 위한 시작점과 끝점
start = 0
end = max(array)

# 이진 탐색 수행
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    
    for x in array:
        if x > mid:
            total += mid
        else:
            total += x

    if total > M:
        end = mid-1
    else:
        result = mid
        start = mid + 1

print(result)
