arr = [5,6,7,8,9]
curr_max = 0
sun = 0

for i in arr:
    if i > curr_max:
        curr_max = i
        sun += 1

print(sun)