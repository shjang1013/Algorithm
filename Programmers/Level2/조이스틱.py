# 나의 코드
def solution(name):
    answer = 0
    
    for i in range(len(name)):
        up = ord(name[i]) - ord('A')
        down = ord('Z') - ord(name[i]) + 2
        answer += min(up, down)
    
    # 조이스틱 조작 횟수의 최솟값을 리턴 
    return answer
