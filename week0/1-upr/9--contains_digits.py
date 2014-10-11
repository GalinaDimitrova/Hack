def contains_digit(number, digit):
    if number != 0:
        if number % 10 == digit:
            return True
        else:
            number = number // 10
            return contains_digit(number, digit)
    else:
        return False


def contains_digits(number, digits):
    if digits == []:
        print(True)
        return True
    else:
        for i in digits:
            if contains_digit(number, i) != True:
                print(False)
                return False
        print(True)
        return True

contains_digits(402123, [0, 3, 4])
contains_digits(666, [6, 4])
contains_digits(123456789, [1, 2, 3, 0])
contains_digits(456, [])
