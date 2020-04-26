def solution(n, lost, reserve):
    answer = 0
    
    student = [0]*n
    
    # 도난당한 학생
    for i in lost:
        student[i-1] -= 1
    
    # 여벌의 체육복을 가져온 학생
    for i in reserve:
        student[i-1] += 1

    for i in range(0, n):
        # 앞에 있는 학생
        if student[i] == 1:
            if i-1 >= 0:
                if student[i-1] == -1:
                    student[i-1] += 1
                    student[i] -= 1

        # 뒤에 있는 학생
        if student[i] == 1:
            if i+1 < n:
                if student[i+1] == -1:
                    student[i+1] += 1
                    student[i] -= 1

    return n-student.count(-1)
