import itertools

def solution(answers):
    student = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    score = []
    answer = []
    
    for i in student:
        count = 0
        # cycle(iterable) : 반복 가능한 요소가 모두 없어질 때까지 무한정 반복
        for j, ans in zip(itertools.cycle(i), answers):
            if j == ans:
                count += 1
        score.append(count)
    
    for i in range(3):
        if score[i] == max(score):
            answer.append(i+1)

    return answer
