# 나의 풀이
def solution(prices):
    # 초 단위로 기록된 주식가격이 담긴 배열 prices # 가격이 떨어지지 않은 기간을 리턴
    answer = [0]*len(prices)
    
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            # 가격이 떨어졌을 경우
            if prices[i] > prices[j]:
                break

    return answer
