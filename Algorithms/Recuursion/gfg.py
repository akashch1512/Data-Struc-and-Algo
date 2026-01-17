# https://www.geeksforgeeks.org/dsa/reduce-a-number-to-1-by-performing-given-operations/


def odd(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + odd(n // 2)
    else:
        return 1 + min(odd(n + 1),odd(n - 1))
    
n = int(input("Enter Num: "))
print(odd(n))

