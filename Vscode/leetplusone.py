def plusOne(digits):
    max = 0
    for digit in digits:
        if max < digit:
            max = digit
    
    idx = digits.index(max)
    digits[idx] += 1

    return digits

def plusoneactual(digits):
    a = int("".join(map(str,digits)))
    a += 1
    a = list(str(a))
    return a
print(plusoneactual([1,4,9]))