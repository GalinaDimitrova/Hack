def prepare_meal(number):
    i = 0
    num = number
    result = ""
    while num % 3 == 0:
        i += 1
        num /= 3
    if i == 1:
        result = "spam"
    if i > 1:
        result += "spam " * (i-1) + "spam"
    if number % 5 == 0:
        if result == "":
            result += "eggs"
        else:
            result = result + "and eggs"
    return(result)
