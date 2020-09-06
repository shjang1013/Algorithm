# 에라토스테네스의 체
# K번째 지워진 수를 출력하기

에라토스테네스의 체
1. 2부터 N까지 모든 정수를 적는다.
2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
3. P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
4. 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.

# 나의 코드
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

a = [False, False] + [True] * (N-1)

List = []
for i in range(2, N+1):
    if a[i]:
        List.append(i)
        for j in range(2*i, N+1, i):
            # 중복되는 수 제외 
            if j not in List:
                List.append(j)
            a[j] = False

print(List[K-1])

