# 팰린드롬
names = input()
name_count = [0 for _ in range(26)]

for name in names:
    name_count[ord(name)-65] += 1

odd = 0
odd_str = ''
string = ''

for i in range(26):
    if name_count[i] % 2 == 1:
        odd += 1
        odd_str += chr(i+65)
    string += chr(i+65) * (name_count[i]//2)

# 홀수개의 알파벳이 1보다 클 경우는 팰린드롬이 될 수 없음
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(string + odd_str + string[::-1])
