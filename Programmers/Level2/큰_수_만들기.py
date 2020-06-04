# 나의 코드(시간 초과)
import itertools

def solution(number, k):
    answer = []
    for i in list(itertools.combinations(number, len(number) - k)):
        temp = ''
        for j in range(len(i)):
            temp += i[j]
        answer.append(int(temp))
    
    return str(max(answer))

# 수정한 코드
def solution(number, k):
    stack = []
    
    for (i, num) in enumerate(number):
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        
        if k == 0:
            stack += number[i:]
            break
        
        stack.append(num)
    
    # 다른 코드 참고하여 수정(2번)
    if k > 0:
        stack = stack[:-k]
    
    return "".join(stack)

# 숙지할 것
1. enumerate 사용법
2. solution("7777777",2)의 경우도 생각하기
