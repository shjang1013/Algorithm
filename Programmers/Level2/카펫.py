# 나의 코드
import math

def solution(brown, yellow):
    answer = [0, 0]
    
    N = brown + yellow
    
    for i in range(1,int(math.sqrt(N))+1):
        if N % i == 0:
            h, v = N // i, i
            
            if (h-2)*(v-2) == yellow:
                answer = [h, v]
                break

    return answer
