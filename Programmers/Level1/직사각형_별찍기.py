# 나의 코드
a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print("*", end='')
    print()

# 다른 사람의 코드
a, b = map(int, input().strip().split(' '))
answer = ('*' * a + '\n') * b
print(answer)
