# 1번 째 방법
test_case = list(map(int, input().split()))

mixed = False

for i in range(len(test_case)-1):
    if abs(test_case[i] - test_case[i+1]) != 1:
        mixed = True

if not mixed:
    if test_case[0] == 1:
        print("ascending")
    else:
        print("descending")
else:
    print("mixed")

# 2번 째 방법
test_case = list(map(int, input().split()))

if test_case == sorted(test_case):
    print("ascending")
elif test_case == sorted(test_case, reverse = True):
    print("descending")
else:
    print("mixed")
