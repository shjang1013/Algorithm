# 나라야나 판디타가 고안한 사전식 순열에서 다음 번 순열을 찾는 알고리즘
import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

# 주어진 순열의 다음에 오는 순열
k = -1

# 1. a[k] < a[k+1]가 성립하는 k의 최댓값 찾기
for i in range(N-1):
    if array[i] < array[i+1]:
        k = i

# 2. k값이 존재하지 않는다면 이미 내림차순
if k == -1:
    print(-1)
else:
    # 3. k 이후의 값들 중 a[k] < a[m]이 성립하는 m의 최댓값 찾기
    for j in range(k+1, N):
        if array[k] < array[j]:
            m = j

    # 4. a[k]와 a[m] 값 바꾸기
    array[k], array[m] = array[m], array[k]

    # 5. k값 이후부터 오름차순으로 정렬
    array = array[:k+1] + sorted(array[k+1:])
    
    print(' '.join(map(str, array)))


