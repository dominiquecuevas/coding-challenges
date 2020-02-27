def plus_one(digits):
    digits[-1] += 1
    for i in range(len(digits)-1, -1, -1):
        if digits[i] >= 10:
            digits[i] = digits[i] -10
            if i != 0:
                digits[i-1] += 1
            else:
                digits.insert(0, 1)
    return digits
print(plus_one([1,2,3]))
print(plus_one([9]))
print(plus_one([9,9]))