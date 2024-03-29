# 메뚜기 정찰병들은 일직선상에 존재하는 식량창고 중에서 서로 인접한 식량 창고가 공격받으면 바로 알아챌 수 있다.
# 따라서 개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량 창고를 약탈해야 한다.

# 문제 해설
1. 왼쪽부터 차례대로 식량창고를 털지 안 털지를 결정하는 경우
2. 특정한 i번째 식량창고에 대해서 털지 안 털지의 여부를 결정할 때
    2-1. (i-1)번째 식량창고를 털기로 결정한 경우 i번째의 식량창고를 털 수 없다.
    2-2. (i-2)번째 식량창고를 털기로 결정한 경우 i번째의 식량창고를 털 수 있다.

# 정수 N 입력받기
N = int(input())

# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1001

# 다이나믹 프로그래밍 진행
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, N):
    d[i] = max(d[i-1], d[i-2] + array[i])

# 계산된 결과 출력
print(d[N-1])
