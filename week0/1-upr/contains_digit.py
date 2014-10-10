def contains_digit(number, digit):
    if number != 0:
        if number % 10 == digit:
            print(True)
            return True
        else:
            number = number // 10
            return contains_digit(number, digit)
    else:
        print(False)
        return False
            



contains_digit(123, 4)
contains_digit(42, 2)
contains_digit(1000, 0)
contains_digit(12346789, 5)
