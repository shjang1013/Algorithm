# left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return
def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        n = i ** 0.5

        # 제곱근이 정수인 경우, 약수의 개수가 홀수
        if int(n) == n:
            answer -= i
        else:
            answer += i

    return answer