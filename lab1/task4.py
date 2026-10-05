sec = int(input())
h = sec // 3600
m = (sec - h * 3600) // 60
s = sec - h * 3600 - m * 60
print(f'{h:02d}:{m:02d}:{s:02d}')