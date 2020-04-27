def solution(arr):
    n = arr[0]
    answer = [n]
    
    # 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return
    for i in arr[1:]:
        if n != i:
            answer.append(i)
            n = i

    return answer
