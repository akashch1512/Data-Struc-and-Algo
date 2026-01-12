# Find 1st Max and 2nd Max in an array in single traversal

l = [1,2,3,4,5,6,7,8,9,10,11]
max1 = 0
max2 = 0

for i in l:
    if i > max1:
        max2 = max1
        max1 = i
    elif max1 > i > max2:
        max2 = i
    
print(f"2nd Max element is {max2}")