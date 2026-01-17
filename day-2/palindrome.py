s = "cabbad" # 6
m = 0

for i in range(len(s)):
    l,r = i,i # 1
    while l >= 0 and r < len(s) and s[l] == s[r]:
        m = max(m,r - l + 1) # 1
        l -= 1 # 0
        r += 1 # 2
    
    l, r = i, i + 1
    while l >=0 and r < len(s) and s[l] == s[r]:
        m = max(m,r - l + 1)
        l -= 1
        r+= 1 
print(m)