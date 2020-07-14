# N번째 손님에게 배정되어야 하는 방 번호
import math

T = int(input())

for _ in range(T):
    H, W, guest = map(int, input().split())
    
    ho = math.ceil(guest/H)
    
    # 층수 : guest % H, 호수 : ho
    if guest%H == 0:
        print(H*100+ho)
    else:
        print((guest%H)*100+ho)
