# 떡의 개수와 떡의 길이 입력받기
N, M = map(int, input().split())

# 각 떡의 높이 입력받기
rice = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점
start = 0
end = max(rice)

# 이진 탐색 수행
result = 0

while start <= end:
    sum = 0
    mid = (start+end) // 2
    
    for i in rice:
        if i > mid:
            sum += x-mid
    
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if sum < M:
        end = mid-1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid
        start = mid+1

print(result)
