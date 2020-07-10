# 종말의 숫자란 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수를 말한다.
# 첫 번째 666으로 시작해 숫자 하나씩 증가시키기
N = int(input())
movie = 666

while N:
    if "666" in str(movie):
        N -= 1
    movie += 1

print(movie - 1)
