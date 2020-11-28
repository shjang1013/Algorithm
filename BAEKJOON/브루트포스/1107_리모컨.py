# 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지 출력하기
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
broken = list(input().split())

# 고장난 버튼을 눌렀는지 확인
def check(i):
    for k in str(i):
        if k in broken:
            return False
    return True

# 채널 100번에서 시작
result = abs(N-100)

# 최소 몇 번을 눌러야 하는지 찾기 
for i in range(1000001):
    if check(i):
        result = min(result, len(str(i))+abs(i-N))

print(result)
