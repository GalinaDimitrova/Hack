def number_to_list(n):
    result = []
    while n > 0:
        result.insert(0,n%10)
        n = n//10
    print(result)
    return result

number_to_list(123)
number_to_list(99999)
number_to_list(123023)