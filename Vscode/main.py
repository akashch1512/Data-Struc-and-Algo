import os

print("Welcome to my X and O game")
a = [ [0,0,0]
     ,[0,0,0]
     ,[0,0,0]]

def printtable():
    for i in range(0,3):
        for k in range(0,3):
            print(a[i][k],end=" ")
        print()


for i in range(100):
    printtable()
    print("Play Player 0")
    a[int(input("Enter ith index"))][int(input("Enter jth index"))] = -1

    print("Play Player 1")
    a[int(input("Enter ith index"))][int(input("Enter jth index"))] = 1
    # 0 0 0
    if(a[0][0] == a[0][1] == a[0][2] == -1):
        print("Player 1 wins")
    if(a[0][0] == a[0][1] == a[0][2] == 1):
        print("Player 0 wins")

    # 1 1 1
    if(a[1][0] == a[1][1] == a[1][2] == -1):
        print("Player 1 wins")
    if(a[1][0] == a[1][1] == a[1][2] == 1):
        print("Player 0 wins")

    # 2 2 2
    if(a[2][0] == a[2][1] == a[2][2] == -1):
        print("Player 1 wins")
    if(a[2][0] == a[2][1] == a[2][2] == 1):
        print("Player 0 wins")

    # 0
    # 0
    # 0
    if(a[0][0] == a[1][0] == a[2][0] == -1):
        print("Player 1 wins")
    if(a[0][0] == a[1][0] == a[2][0] == 1):
        print("Player 0 wins")

    # 1
    # 1
    # 1
    if(a[0][1] == a[1][1] == a[2][1] == -1):
        print("Player 1 wins")
    if(a[0][1] == a[1][1] == a[2][1] == 1):
        print("Player 0 wins")

    # 2
    # 2 
    # 2
    if(a[0][2] == a[1][2] == a[2][2] == -1):
        print("Player 1 wins")
    if(a[0][2] == a[1][2] == a[2][2] == 1):
        print("Player 0 wins")


    if(a[0][0] == a[1][1] == a[2][2] == -1):
        print("Player 1 wins")
    if(a[0][0] == a[1][1] == a[2][2] == 1):
        print("Player 0 wins")

    if(a[0][2] == a[1][1] == a[2][0] == -1):
        print("Player 1 wins")
    if(a[0][2] == a[1][1] == a[2][0] == 1):
        print("Player 0 wins")

    os.system('clear')