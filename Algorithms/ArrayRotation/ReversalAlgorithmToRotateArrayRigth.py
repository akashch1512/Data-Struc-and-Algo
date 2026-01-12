# (Reversal Algorithm) ⭐⭐
# rotate array k postions to the Rigth

a = [1,2,3,4,5]

k = int(input("Enter value: "))
k %= len(a)

def reverse(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

reverse(a, 0, len(a)-1)
reverse(a, 0, k-1)
reverse(a, k, len(a)-1)

print(a)
