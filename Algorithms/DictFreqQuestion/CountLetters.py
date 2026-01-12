# Count Freq of Char in an String using Dict

data = "akashismyname"
dic = dict()

for i in range(len(data)):
    if data[i] not in dic:
        dic[data[i]] = 1
    else:
        dic[data[i]] += 1
    
print(dic)
