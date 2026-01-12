
def buyChoco(prices,money):

    min1 = float("+inf") # 98 54 6
    min2 = float("+inf") # i 98 54
    # optimized

    for i in prices:
        if i < min1:
            min2 = min1
            min1 = i 
        elif min2 > i :
            min2 = i
            
    # print(min1,min2) 

    # with two loops

    if min1+min2 > money:
        return money        
    return money - (min1+min2) 

    # with two loops

print(buyChoco([41,1,28,2,92,97,1,87],68))