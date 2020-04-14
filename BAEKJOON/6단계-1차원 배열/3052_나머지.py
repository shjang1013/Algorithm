test_case = []
for i in range(10):
    test_case.append(int(input())%42)

test_case = set(test_case)
print(len(test_case))
