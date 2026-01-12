# Finding 1st min and 2nd min in an array in single traversal

l = [11,10,1,2,3,4,8,5,2,6,1,2,5]
min1 = float('inf')
min2 = float('inf')

for i in l:
    if i < min1:
        min2 = min1
        min1 = i
    elif i < min2 and i != min1:
        min2 = i

    # Other Simpler Alternative
    # elif min1 < i < min2:
    #     min2 = i


print(f"The 2nd minimum value from the list is {min2}")