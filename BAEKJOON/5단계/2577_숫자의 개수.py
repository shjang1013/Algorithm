a = int(input())
b = int(input())
c = int(input())

mul = str(a*b*c)

# count를 사용하여 개수 구하기
for i in range(0,10):
    print(mul.count(str(i)))
