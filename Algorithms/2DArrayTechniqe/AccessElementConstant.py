mat = [
    [1,2,3,4],
    [5,6,7,8],
    [9,6,1,5]
]

num_of_colm = len(mat[0]) # 4

# assume we want to traverse till 6 th index (0 indexed)
index = 6 # value 7 

index1 = index // num_of_colm
index2 = index % num_of_colm

print(index1,index2)

# So you can easily acess that element
print(mat[index1][index2])