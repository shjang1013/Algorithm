# n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return
def solution(n):
    answer = 0
    num = ''

    while n >= 3:
        num = str(n % 3) + num
        n //= 3

    ternaryList = list(str(n) + num)

    for i in range(len(ternaryList)):
        answer += int(ternaryList[i]) * (3 ** i)

    return answer