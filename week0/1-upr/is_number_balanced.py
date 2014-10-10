
def sum_of_digits(n):
    n = abs(n)
    result = 0
    while n > 0:
        result += n%10
        n = n // 10
    return result


def is_number_balanced(n):
    if n < 10:
        print(True)
        return True
    else:
        str_num = n
        # Get lenght of the integer
        lenght = len(str(str_num)) 
        # Check if the number is not with odd lenght
        if lenght % 2 == 0:
            suff = n % 10**(lenght // 2)
            pref = n // 10**(lenght // 2)
            if sum_of_digits(suff) == sum_of_digits(pref):
                print(True)
                return True
            else:
                print(False)
                return False
        else:
            # if the number is with odd lenght, to get the  \ 
            # prefix we should divide it to 10**(lenght // 2 + 1) 
            suff = n % 10**(lenght // 2)
            pref = n // 10**(lenght // 2 + 1)
            if sum_of_digits(suff) == sum_of_digits(pref):
                print(True)
                return True
            else:
                print(False)
                return False




is_number_balanced(9)
is_number_balanced(11)
is_number_balanced(13)
is_number_balanced(121)
is_number_balanced(4518)
is_number_balanced(28471)
is_number_balanced(1238033)