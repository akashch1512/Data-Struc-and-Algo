
# fire can spread thourgh trees = 1 not by land = 0

# fire can spread thorough up down rigth left

# return the num of unbured tree if burning starting point is given as k
# mat is given for forest 

def wildfire(mat,i,j):
    if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]) or mat[i][j] != 1:
        return
    mat[i][j] = 0
    wildfire(mat,i-1,j)
    wildfire(mat,i+1,j)
    wildfire(mat,i,j+1)
    wildfire(mat,i,j-1)

i,j = map(int, input("Enter Start: ").split())
mat = [[1,1,1,0],
       [1,1,0,1],
       [0,0,0,1],
       [1,1,0,0]]

wildfire(mat,i,j)

total_1 = 0
for i in mat:
    total_1 += sum(i)
print(total_1)


