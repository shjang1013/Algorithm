# 문제
# SWEA 4839 - [파이썬 S/W 문제해결 기본 2일차] LIST2 - 이진탐색

# 나의 코드(실패) - 10개의 input 중 8개의 input만 정답
# 이진탐색
def binarySearch(P, key):
    count = 1
    l = 1
    r = P
    while l <= r:
        c = int((l+r)/2)
        if key == c: # 탐색성공
            return count
        elif key < c:
            count += 1
            r = c-1
        else:
            count += 1
            l = c+1
    return False # 탐색실패

T = int(input())

for tc in range(T):
    # 전체 쪽 수, 찾을 쪽 번호 A, B
    P, A, B = map(int, input().split())
    countA = binarySearch(P, A)
    countB = binarySearch(P, B)
    
    # 탐색에 실패했을 경우 or 비긴 경우
    if countA == False or countB == False or countA == countB:
        result = '0'
    
    # count의 횟수가 작을 때 출력 => 이긴 경우
    elif countA < countB:
        result = 'A'
    else:
        result = 'B'
    
    print('#{0} {1}' .format(tc+1, result))


# 수정한 코드(강의에서 이진탐색의 경우 중간값에 +1 또는 -1한 값을 넣어주었는데 이 문제의 경우 중간값을 넣어줌)
# 이진탐색
def binarySearch(P, key):
    count = 1
    l = 1
    r = P
    while l <= r:
        c = int((l+r)/2)
        if key == c: # 탐색성공
            return count
        elif key < c:
            count += 1
            r = c # 중간값을 넣어줄 것
        else:
            count += 1
            l = c
    return False # 탐색실패

T = int(input())

for tc in range(T):
    # 전체 쪽 수, 찾을 쪽 번호 A, B
    P, A, B = map(int, input().split())
    countA = binarySearch(P, A)
    countB = binarySearch(P, B)
    
    # 탐색에 실패했을 경우 or 비긴 경우
    if countA == False or countB == False or countA == countB:
        result = '0'
    
    # count의 횟수가 작을 때 출력 => 이긴 경우
    elif countA < countB:
        result = 'A'
    else:
        result = 'B'
    
    print('#{0} {1}' .format(tc+1, result))

