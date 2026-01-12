a = [1,1,1,1,1,1,1,1,2,2,2,3,3,3,3,1,1,1,1,1]

candidate = a[0]
votes = 0

for i in a:
    if votes == 0:
        candidate = i
    if i == candidate:
        votes += 1 
    else:
        votes -= 1

# Understand that it only shows correct if the element apperes more then len(arr) / 2 or more times
print(f"The element which appered in majority is {candidate}")