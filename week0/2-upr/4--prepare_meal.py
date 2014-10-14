def prepare_meal(number):
    i = 0
    num = number
    result = ""
    while num % 3 == 0:
        i += 1
        num /= 3
    if i > 0:
        result += "spam " * i
    if number % 5 == 0:
        if result == "":
            result += "eggs"
        else:
            result = result + "and eggs"
    print(result)
    return(result)

prepare_meal(3)
prepare_meal(27)
prepare_meal(7)
prepare_meal(5)
prepare_meal(15)
prepare_meal(45)
