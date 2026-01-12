a = list(map(int,input("Enter Elements").split()))
# for i in a:
#     cou = int(a.count(i))
#     if cou > 1:
#         for j in range(cou-1):
#             a.remove(i)
    
# print(a)

# O(n**2)

ans = []
for i in a:
    if i not in ans:
        ans.append(i)
print(ans)



