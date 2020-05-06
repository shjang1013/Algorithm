# 나의 코드
import math

def solution(progresses, speeds):
    answer = []
    day = [0] * len(progresses)
    
    for i in range(len(progresses)):
        day[i] = math.ceil((100-progresses[i])//speeds[i])

    # 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞은 있는 기능이 배포될 때 함꼐 배포
    for i in range(1, len(day)):
        if day[i-1] > day[i]:
            day[i] = day[i-1]

    count = 1
    for i in range(1, len(day)):
        if day[i-1] == day[i]:
            count += 1
        else:
            answer.append(count)
            count = 1

    answer.append(count)
    return answer


# 추가 테스트케이스
progresses : [40, 93, 30, 55, 60, 65]
speeds : [60, 1, 30, 5 , 10, 7]
return : [1,2,3]

progresses : [93, 30, 55, 60, 40, 65]
speeds : [1, 30, 5 , 10, 60, 7]
return : [2,4]
