N = int(input())

array = input()

nums = [int(input()) for _ in range(N)]

stack = []

for i in range(len(array)):
    if array[i].isalpha():
        n = ord(array[i])-ord('A')
        stack.append(nums[n])
    else:
        a = stack.pop()
        b = stack.pop()
        
        if array[i] == '*':
            temp = b*a
        elif array[i] == '+':
            temp = b+a
        elif array[i] == '/':
            temp = b/a
        elif array[i] == '-':
            temp = b-a

        stack.append(temp)

# 계산 결과를 소숫점 둘째 자리까지 출력하기
print(f"{stack[0]:.2f}")
