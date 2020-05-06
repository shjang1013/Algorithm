# 나의 코드(시간초과)
def solution(bridge_length, weight, truck_weights):
    # 시간
    answer = 0
    # 다리를 건너는 트럭
    passing = [0] * bridge_length
    
    while passing:
        answer += 1
        passing.pop(0)
        if truck_weights:
            if sum(passing) + truck_weights[0] <= weight:
                passing.append(truck_weights.pop(0))
            else:
                passing.append(0)

    return answer

# 문제점
1. passing 리스트가 bridge_length 만큼 차지
2. truck_weights.pop(0)은 첫 번째 원소를 빼고 그 뒤에 원소들을 한 칸씩 앞으로 땡겨줘야 하기 때문에 O(n) 만큼 걸림
    => truck_weights.pop() : O(1)

# 다시 풀기
# deque() 이용
