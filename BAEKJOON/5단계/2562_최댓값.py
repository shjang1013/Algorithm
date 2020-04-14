# 1번 째 방법
test_case = []

for _ in range(9):
    test_case.append(int(input()))

print(max(test_case))
print(test_case.index(max(test_case))+1)

# 2번 째 방법
max_num = 0
max_index = 0

for i in range(9):
    a = int(input())

    if(a > max_num):
        max_num = a
        max_index = i+1

print('%d\n%d\n' %(max_num, max_index))

