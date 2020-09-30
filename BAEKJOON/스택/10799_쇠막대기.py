# 잘려진 조각의 총 개수 출력하기
bar = input()
sum = 0
stack = []

bar = bar.replace('()', 'L')

for i in bar:
    if i == '(':
        stack.append('(')
    elif i == ')':
        sum += 1
        stack.pop()
    else:
        sum += len(stack)

print(sum)
