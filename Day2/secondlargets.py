# find the second larget number from the array

arr = [98,54,6,34,66,63,52,39]

max1 = 0
max2 = 0
# optimized

for i in arr:
    if i > max1:
        max2 = max1
        max1 = i
    elif max2 < i and max1 != i:
        max2 = i
        
print(max1+max2) 

# with two loops
