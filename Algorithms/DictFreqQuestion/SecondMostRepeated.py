# return the 2 nd most repeated letter in an string

data = "akashismyname"
dic = dict()

for i in range(len(data)):
    if data[i] not in dic:
        dic[data[i]] = 1
    else:
        dic[data[i]] += 1
    
max1 = max2 = 0
letter1 = letter2 = ''

for ch, count in dic.items():
    if count > max1:
        max2, letter2 = max1, letter1
        max1, letter1 = count, ch

    elif max2 < count < max1:
        max2, letter2 = count, ch

if letter2:
    print(f"2nd Most Repeated Letter is '{letter2}' repeated {max2} times")
else:
    print("No 2nd most repeated letter exists")