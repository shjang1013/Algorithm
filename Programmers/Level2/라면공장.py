# 나의 코드
import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    idx = 0
    queue = []
    
    while stock < k:
        for i in range(idx, len(dates)):
            if stock < dates[i]:
                break
            # 최대 힙 
            heapq.heappush(queue, -supplies[i])
            idx = i + 1
    
        stock += (heapq.heappop(queue) * -1)
        answer += 1

    return answer
