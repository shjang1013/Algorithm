def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        sorted_list = sorted(array[i - 1:j])
        answer.append(sorted_list[k-1])
    
    return answer
