# Finding minimum member in an array

l = [11,10,1,2,3,4,8,5,2,6,1,2,5]
min = float('inf')

for i in l:
    if i < min:
        min = i

print(f"The minimum value from the list is {min}")