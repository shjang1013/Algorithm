# 내림차순으로 정렬하기 
N = int(input())

List = sorted(list(str(N)), reverse=True)

print(''.join(List))
