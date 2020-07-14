# 더 적은 개수의 봉지를 배달하기 위해 5킬로그램의 설탕을 가져가도록 한다
# 5킬로그램의 설탕 봉지를 1씩 감소시키며 봉지의 최소 개수 계산
N = int(input())

for i in range(N//5, 0, -1):
    if (N-i*5) % 3 == 0:
        print(i + (N-i*5)//3)
        break
else:
    print(N//3) if N%3 == 0 else print(-1)
