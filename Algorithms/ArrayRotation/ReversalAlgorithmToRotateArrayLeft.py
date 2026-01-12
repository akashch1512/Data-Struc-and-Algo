# rotate array k postions to the left

li = [1,2,3,4,5]

k = int(input("Enter Rotation Amount"))
k %= len(li)
k -= 1

def rev(arr,l,r):
    while l < r:
        print("hi")
        arr[l], arr[r] = arr[r], arr[l]
        
        l += 1
        r -= 1
    
rev(li,0,k)
rev(li,k+1,len(li)-1)
rev(li,0,len(li)-1)

print(li)