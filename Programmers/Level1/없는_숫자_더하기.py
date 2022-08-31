# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return
def solution(numbers):
    answer = 0

    for i in range(10):
        if i not in numbers:
            answer += i

    return answer