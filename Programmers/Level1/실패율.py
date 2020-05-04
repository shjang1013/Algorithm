# 나의 코드
def solution(N, stages):
    answer = []
    user = len(stages)
    for i in range(1, N + 1):
        if i in stages:
            answer.append((i, stages.count(i) / user))
            user -= stages.count(i)
        else:
            # 스테이지에 도달한 유저가 없는 경우
            answer.append((i, 0))

    # 실패율이 높은 스테이지부터 내림차순으로 정렬
    answer = sorted(answer, key=lambda x: -x[1])

    return [answer[i][0] for i in range(N)]


# 딕셔너리를 이용한 코드
def solution(N, stages):
    result = {}
    user = len(stages)
    for stage in range(1, N+1):
        if user != 0:
            count = stages.count(stage)
            result[stage] = count / user
            user -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)


# collections.Counter()를 이용해서 구해볼 것
