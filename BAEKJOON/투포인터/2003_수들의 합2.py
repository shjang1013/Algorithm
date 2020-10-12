# 수열의 i번째 수부터 j번째 수까지의 합이 M이 되는 경우의 수를 출력하기

특정한 합을 가지는 부분 연속 수열 찾기
1. 문제 해결 방법
    - 투 포인터 방법 : 리스트에 순차적으로 접근해야 할 때 두 개의 점을 이용해 위치를 기록하면서 처리하는 기법
2. 투 포인터를 활용한 알고리즘 설명
    - 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스(0)를 가리키도록 한다.
    - 현재 부분 합이 M과 같다면, 카운트한다.
    - 현재 부분 합이 M보다 작다면, end를 1 증가시킨다.
    - 현재 부분 합이 M보다 크다면, start를 1 증가시킨다.
    - 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다.


# 코드
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

array = list(map(int, input().split()))

end = 0
sum = 0
count = 0

# start를 차례대로 증가시키며 반복
for start in range(N):
    # end를 가능한 만큼 이동시키기
    while sum < M and end < N:
        sum += array[end]
        end += 1
    # 부분 합이 m일 때 카운트 증가
    if sum == M:
        count += 1
    
    sum -= array[start]

print(count)
