# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K가 주어진다. 이제 순서대로 K번째 사람을 제거한다.
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
N, K = map(int, input().split())

queue = [i for i in range(1, N+1)]

List = []

i = K-1

while len(queue):
    List.append(queue.pop(i))
    if queue:
        # 앞의 숫자를 하나 제거 => K-1
        i = (i+K-1) % len(queue) # 반복할 때는 % 사용하기

print('<'+', '.join(map(str, List))+'>')
