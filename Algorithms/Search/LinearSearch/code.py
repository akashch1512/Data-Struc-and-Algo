# Find element k from an list 

l = [1,2,3,45,6,7,8,5]
k = 9

for i in l:
    if i == k:
        print(f"{k} Found at index {i}")
        break
# else work in loop only a loop is 100% complets itself and last condition is false
else: 
    print(f"{k} is not present")