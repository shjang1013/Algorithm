# N개를 만들 수 있는 랜선의 최대 길이 
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
LAN = [int(input()) for _ in range(K)]

start = 1
end = sum(LAN) // N

result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    
    for i in LAN:
        count += (i // mid)
    
    if count >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
