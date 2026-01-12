# print the element in the list which has occured odd number of times

l = [7,1,2,4,3,5,6] 

l.sort()
res = []
for i in l:
    if i%2!=0:
        res.append(i)
    else:
        res.insert(0,i)
print(res)       