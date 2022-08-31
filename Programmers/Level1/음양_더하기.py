# 실제 정수들의 합을 구하여 return : signs[i]가 참이면 absolutes[i]의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미
def solution(absolutes, signs):
    for i in range(len(signs)):
        # 양수
        if signs[i]:
            continue
        # 음수
        else:
            absolutes[i] = (-1) * absolutes[i]

    return sum(absolutes)