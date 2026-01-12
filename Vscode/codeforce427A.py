n = int(input("Enter How Many?"))
arr = list(map(int,input("Enter Crime").split()))
police = 0
crime = 0

for i in range(n):
    if arr[i] > 0:
        police += arr[i]
    else:
        if police and arr[i] == -1:
            police -= 1
        
        elif not police and arr[i] == -1:
            crime += 1
    
print(crime)