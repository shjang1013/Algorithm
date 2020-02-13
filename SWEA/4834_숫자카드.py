# 문제
# SWEA 4834 - [파이썬 S/W 문제해결 기본 1일차] LIST1 - 숫자카드

T = int(input())

for i in range(T):
    N = input()
    test_case = list(input())
    card_list = [int(i) for i in test_case]
    count_list = [0] * 10
    for j in card_list:
        count_list[j] += 1  # N개의 숫자 개수대로 +1
            
    max_index, max_num = 0, 0
    for k in range(len(count_list) - 1, -1, -1):  # 카드 장수가 같을 때는 큰 쪽을 출력하기 위해
        if count_list[k] > max_index:
            max_index = count_list[k]
            max_num = k
                            
    print('#{0} {1} {2}'.format(i + 1, max_num, max_index))


