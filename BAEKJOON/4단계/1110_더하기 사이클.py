num = int(input())
new_num = -1
count = 0

new_num = num

while True:
    new_num = (new_num % 10) * 10 + (new_num // 10 + new_num % 10) % 10
    count += 1
    
    if new_num == num:
        break;

print(count)
