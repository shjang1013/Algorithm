# 문제
# SWEA 4835 - [파이썬 S/W 문제해결 기본 1일차] LIST1 - 구간합

# T : 테스트 케이스 개수
T = int(input())

for i in range(T):
    # N : 정수의 개수, M : 구간의 개수
    N, M = map(int, input().split())
    test_case = list(map(int, input().split()))
    # 이웃한 M개의 합을 리스트에 저장
    sum_list = [sum(test_case[j:j+M]) for j in range(N-M+1)]
        
    print('#{0} {1}' .format(i+1, max(sum_list)-min(sum_list)))

