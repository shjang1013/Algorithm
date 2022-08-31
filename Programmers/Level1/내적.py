# a와 b의 내적을 return : a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... +a[n-1]*b[n-1]
def solution(a, b):
    answer = 0

    for i in range(len(a)):
        answer += a[i]*b[i]

    return answer

# zip() 활용
def solution(a, b):
    return sum([x*y for x, y in zip(a, b)])