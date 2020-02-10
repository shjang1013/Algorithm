'''
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다. 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다. 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오. 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

[입력]
첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )

[출력]
#과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.
'''

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



