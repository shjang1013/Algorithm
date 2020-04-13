def solve():
    num_set = set(range(1,10001))
    constructor_set = set()
    
    for i in num_set:
        for j in str(i):
            i += int(j)  # 33 -> 33 + 3 + 3 = 39
        constructor_set.add(i)  # 집합 자료형 값 추가하기

    self_set = num_set - constructor_set  # 차집합

for k in sorted(self_set):
    print(k)

solve()
