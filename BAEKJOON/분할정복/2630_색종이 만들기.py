# 하얀색 색종이의 개수와 파란색 색종이의 개수를 출력하기 
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

def solution(arr):
    answer = [0, 0]
    
    white = 0
    blue = 0
    
    l = len(arr)
    
    def quad(x, y, n):
        if n == 1:
            return
        count = 0
        for i in range(n):
            count += arr[i+x][y:y+n].count(1)
        
        if count == 0 or count == n*n:
            for i in range(n):
                for j in range(n):
                    arr[x+i][y+j] = 2
    
        if count == 0:
            arr[x][y] = 0
        elif count == n*n:
            arr[x][y] = 1
        else:
            quad(x, y, n // 2)
            quad(x + n // 2, y, n // 2)
            quad(x, y + n // 2, n // 2)
            quad(x + n // 2, y + n // 2, n // 2)

    x = y = 0
    
    quad(x, y, l//2)
    quad(x+l//2, y, l//2)
    quad(x, y+l//2, l//2)
    quad(x+l//2, y+l//2, l//2)
    
    for i in range(l):
        white += arr[i].count(0)
        blue += arr[i].count(1)

    answer[0] = white
    answer[1] = blue

    return answer

answer = solution(arr)

print(answer[0])
print(answer[1])
