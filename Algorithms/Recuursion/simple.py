def fun(a,b):
    if a + b == 10:
        return a
    return fun(a-1,b-1)

print(fun(20,20))
n = int(input("Enter int: "))
