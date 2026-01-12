# Return the most repeated letter in an string

data = "akashismyname"
dic = dict()

for i in range(len(data)):
    if data[i] not in dic:
        dic[data[i]] = 1
    else:
        dic[data[i]] += 1
    

max = 0
letter = ''

for i in dic:
    if dic[i] > max:
        max = dic[i]
        letter = i

print(f"Most Repeated Letter is {letter} which is repeated {dic[letter]} times")