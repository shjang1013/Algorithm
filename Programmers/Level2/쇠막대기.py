# 나의 코드
def solution(arrangement):
    # 쇠막대기의 개수
    answer = 0
    # 레이저
    arrangement = arrangement.replace("()", "C")
    stick = 0
    for i in arrangement:
        if i == "(":
            stick += 1
            answer += 1
        elif i == ")":
            stick -= 1
        else:
            answer += stick

    return answer
