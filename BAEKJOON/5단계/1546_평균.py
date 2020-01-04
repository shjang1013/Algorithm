# 입력
num = int(input())
test_case = list(map(int, input().split()))

# 최댓값
M = max(test_case)

# 현재 성적의 평균
avg = sum(test_case)/num

# 새로운 평균
new_avg = avg/M*100
print(round(new_avg,2))
