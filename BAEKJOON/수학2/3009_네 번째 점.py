# 직사각형 경계선까지 가는 거리의 최솟값을 출력
x, y, w, h = map(int, input().split())

print(min([x, y, w-x, h-y]))
