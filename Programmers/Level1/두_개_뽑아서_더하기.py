# numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return
def solution(numbers):
    SUM = set()

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            SUM.add(numbers[i] + numbers[j])

    answer = sorted(list(SUM))

    return answer
