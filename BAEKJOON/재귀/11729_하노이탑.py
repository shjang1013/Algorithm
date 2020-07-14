'''
하노이탑의 이동 규칙

n개의 원판이 있을 때, n-1개의 원판 즉, 맨 밑의 원판을 제외하고 나머지 원판들을
1번에서 2번으로 옮긴 뒤, 맨 밑의 원판을 1번에서 3번으로 옮긴다.
그리고 n-1개의 원판들을 다시 2번에서 3번으로 옮긴다.
'''

# 하노이탑
def Hanoi(N, start, mid, end):
    if N == 1:
        print(start, end)
    else:
        Hanoi(N - 1, start, end, mid)
        print(start, end)
        Hanoi(N - 1, mid, start, end)

T = int(input())

min = 0
for i in range(T):
    min = min * 2 + 1
print(min)

Hanoi(T, 1, 2, 3)


