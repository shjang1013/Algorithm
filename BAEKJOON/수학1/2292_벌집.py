# 1 7 19 37 61 ...
# 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지

N = int(input())
num = count = 1

while num < N:
    num += count * 6
    count += 1

print(count)
