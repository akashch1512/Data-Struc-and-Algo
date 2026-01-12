l = [1,1,2,1,2,1,2,1,5,1,1,5]
d = {}

for i in range(len(l)):
    if l[i] not in d:
        d[l[i]] = 1
    else:
        d[l[i]] += 1 

        
max = 0
max2 = 0
ele = 0 
for i in d:
    if d[i] > max:
        max = d[i]
        ele = i
    
    if d[i] :
        max = 
    
print(ele)