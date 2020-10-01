# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력하기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

Tree = list(map(int, input().split()))

start= 0
end = max(Tree)
result = 0

while start <= end:
    t = 0
    mid = (start+end) // 2
    for i in Tree:
        if i > mid:
            t += (i-mid)
    if t < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
