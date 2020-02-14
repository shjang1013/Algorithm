# 문제
# SWEA 4843 - [파이썬 S/W 문제해결 기본 2일차] LIST2 - 특별한 정렬

# 나의 코드(오답)
T = int(input())

for tc in range(T):
    N = int(input())
    test_list = list(map(int, input().split()))
    
    # 정렬된 리스트
    sort_list = sorted(test_list)
    
    print('#{0}' .format(tc+1), end=' ')
    
    for i in range(len(sort_list)):
        # 리스트에서 큰 수 출력
        if i%2==0:
            print(sort_list.pop(len(sort_list)-1), end=' ')
        # 리스트에서 작은 수 출력
        else:
            print(sort_list.pop(0), end=' ')

    print()

# 나의 코드(정답)
T = int(input())

for tc in range(T):
    N = int(input())
    test_list = list(map(int, input().split()))
    
    # 정렬된 리스트
    sort_list = sorted(test_list)

    print('#{0}' .format(tc+1), end=' ')
    
    # N이 10보다 크더라도 10개만 출력하기
    for i in range(10):
        # 리스트에서 큰 수 출력
        if i%2==0:
            print(sort_list.pop(len(sort_list)-1), end=' ')
        # 리스트에서 작은 수 출력
        else:
            print(sort_list.pop(0), end=' ')

    print()

# 수정한 코드(다른 코드 참고)
T = int(input())

for tc in range(T):
    N = int(input())
    test_list = list(map(int, input().split()))
    special_list = [0]*N

    # max 값 구하기
    for i in range(N//2):
        special_list[i*2] = test_list.pop(test_list.index(max(test_list)))

    # min 값 구하기
    for i in range(N//2):
        special_list[i*2+1] = test_list.pop(test_list.index(min(test_list)))

    print('#{0} ' .format(tc+1))

    for i in range(10):
        print(special_list[i], end=' ')

    print()
