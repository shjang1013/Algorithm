# 문제
# SWEA 4831 - [파이썬 S/W 문제해결 기본 1일차] LIST1 - 전기버스

bus = int(input())

for i in range(1, bus+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    bus_place = 0 # 버스 현재 위치
    end = 0
    start = 0
    charge_count = 0 # 충전 횟수
    status = 0 # 충전기와 버스 현재 위치가 같으면 1, 다르면 0
                        
    while True:
        end += K
        if end < N: # 종점 번호보다 작을 경우
            for j in range(end, start, -1):
                if j in station: # 충전기가 위치하는 정류소에 속할 경우
                    status = 1
                    end = j
                    start = j
                    charge_count += 1
                    break
                else:
                    status = 0
        else:
            break
                                                                                
       if status == 0: # 충전기 설치가 잘못되어 종점에 도착할 수 없는 상황
           charge_count = 0
           break
                                                                                            
    print('#{0} {1}' .format(i, charge_count))



