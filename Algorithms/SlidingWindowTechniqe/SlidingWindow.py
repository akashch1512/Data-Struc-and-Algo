# Find Sum of 3 consecative elements of arr which is highest

a = [1,2,3,4,5,6,4,7,8,5,5]

Sum = a[0] + a[1] + a[2]
Max = Sum
Start = 0

while Start + 3 < len(a):
    Sum = Sum + a[Start + 3] - a[Start]
    Start += 1
    if Sum > Max:
        Max = Sum

print("The maximum 3 length Subarray Addtion is",Max)