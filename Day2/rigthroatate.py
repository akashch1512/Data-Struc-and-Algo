a = [1,2,3,4,5]

temp = a[-1]

for i in range(1,len(a)):
    a[-i] = a[-i-1]

a[0] = temp

print(a)