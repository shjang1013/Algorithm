# 나의 코드
def solution(heights):
    # 각 탑이 쏜 신호를 어느 탑에서 받았는지 기록한 배열을 리턴
    answer = [0] * len(heights)
    
    for i in range(len(heights)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                answer[i] = j+1
                break

    return answer
