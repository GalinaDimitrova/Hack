def list_to_number(digits):
    result = 0
    lenght = len(digits)
    for i in range(lenght,0,-1):
        #First we take the first digit and put it in correct place \
        #than we sum it with the other digits
        result += digits[0]*(10**(i-1))
        #We remove used digit to get the other one
        digits.remove(digits[0])

    print(result)
    return result

list_to_number([1,2,3])
list_to_number([9,9,9,9,9])
list_to_number([1,2,3,0,2,3])
