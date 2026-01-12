l = [9,2,1,2,4]
sum = 0
for i in range(0,len(l),2):
    if i%2 == 0:
        sum += l[i]
    
print(sum)