# 입력
num = int(input())
for _ in range(num):
    count = 0
    test_case = list(map(int, input().split()))
    avg = sum(test_case[1:])/test_case[0]
    
    for j in test_case[1:]:
        # 평균을 넘는 학생의 수
        if avg<j:
            count += 1

print("%.3f%%" %round(count/test_case[0]*100,3))
