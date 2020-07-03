# 분수 출력
# 1/1 1/2 2/1 3/1 2/2 1/3 ....

N = int(input())
s = count = 1

while s <= N:
    s += count
    count += 1

bunsu = count-(s-N)

if count % 2:
    print(str(bunsu)+"/"+str(count-bunsu))
else:
    print(str(count - bunsu) + "/" + str(bunsu))
