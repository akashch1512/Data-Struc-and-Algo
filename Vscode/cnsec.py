l = [1,2,4,3]
def ans():
    curr = 0
    while curr < len(l)-1:
        if l[curr + 1] != l[curr] + 1:
            return False
        curr += 1
    return True

print(ans())