hour,min = map(int, input().split())

if min>=45:
    min = min-45
elif hour == 0:
    hour = 23
    min = min+15
else:
    hour = hour-1
    min = min+15

print(hour,min)
