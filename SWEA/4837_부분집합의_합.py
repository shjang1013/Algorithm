# 문제
# SWEA 4837 - [파이썬 S/W 문제해결 기본 2일차] LIST2 - 부분집합의 합

# 나의 코드
T = int(input())
A = [1,2,3,4,5,6,7,8,9,10,11,12]
A_len = len(A)

for tc in range(T):
    # N : 부분집합 원소의 수, K : 부분 집합의 합
    N, K = map(int, input().split())
    count = 0
    # A의 부분집합
    for i in range(1 << A_len):
        subset_list = []
        for j in range(A_len):
            if i & (1 << j):
                subset_list.append(A[j])
    
        # 부분집합 원소의 수와 부분 집합의 합이 일치하는 경우
        if len(subset_list) == N and sum(subset_list) == K:
            count+=1

    print('#{0} {1}' .format(tc+1, count))

# 수정한 코드
T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
A_len = len(A)

# A의 부분집합 구하기
subset_list = []
for i in range(1 << A_len):
    temp_list = []
    for j in range(A_len):
        if i & (1 << j):
            temp_list.append(A[j])

    subset_list.append(temp_list)

for tc in range(T):
    # N : 부분집합 원소의 수, K : 부분 집합의 합
    N, K = map(int, input().split())
    count = 0
    
    for i in subset_list:
        # 부분집합 원소의 수와 부분 집합의 합이 일치하는 경우
        if len(i) == N and sum(i) == K:
            count += 1

    print('#{0} {1}'.format(tc + 1, count))
