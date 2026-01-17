# LMS Learning Management System

# take n as input
# dont use a loop

# recc is rev of loop

# for ex. 
# 5 4 3 2 1
# 12345
# 5 3 1

# n = 10 8 6 4 2 4 6 8 10

# 1 2 3 4 5 4 3 2 1

def last(n,m=0):
    if n == m:
        return
    print(m+1,end=" ")
    last(n,m+1)
    if m+1 != 5:
        print(m+1,end=" ")

# Tail Recursion
def fun(n):
    if n <= 0:
        return
    print(n, end=" ") 
    fun(n-1)

# Head Recursion
def fun2(n):
    if n <= 0:
        return
    fun2(n-1)
    print(n, end=" ") 

# 
def fun3(n):
    if n <= 0:
        return
    if n % 2 != 0:
        print(n, end=" ") 
    fun3(n-1)

def fun4(n):
    if n <= 0:
        return
    if n % 2 == 0:
        print(n, end=" ") 
    fun4(n-1)
    if n % 2 == 0 and n != 2:
        print(n, end=" ") 

def fun5(n):
    if n <= 0:
        return 200
    t = fun5(n-1)
    print(n, end=" ") 
    return t

n = int(input("Enter the num: "))
print(last(n))
print()