# 문제
# SWEA 4836 - [파이썬 S/W 문제해결 기본 2일차] LIST2 - 색칠하기

# 테스트 케이스 개수
T = int(input())

for i in range(T):
    # 칠할 영역의 개수
    N = int(input())
    red_list = []
    blue_list = []
    for j in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        # 좌표 삽입
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if color == 1:
                    red_list.append((x, y))
                elif color == 2:
                    blue_list.append((x, y))

    # 교집합을 이용하기 위해 set 자료형으로 형변환
    red_set = set(red_list)
    blue_set = set(blue_list)

    # 공통된 튜플의 개수
    purple = len(red_set & blue_set)
    
    print('#{0} {1}' .format(i+1, purple))

