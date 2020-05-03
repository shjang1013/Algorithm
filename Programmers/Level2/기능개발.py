# 나의 코드
def solution(progresses, speeds):
    answer = []
    day = []
    count = 0
    for i in range(len(progresses)):
        s = 100 - progresses[i]
        
        if s % speeds[i] == 0:
            day.append(s // speeds[i])
        else:
            day.append(s // speeds[i] + 1) # ceil

    for i in range(1, len(day)):
        if day[i-1] > day[i]:
            day[i] = day[i-1]
    
    count = 1
    for i in range(1, len(day)):
        if day[i-1] >= day[i]:
            count += 1
        else:
            answer.append(count)
            count = 1

    answer.append(count)
    return answer
