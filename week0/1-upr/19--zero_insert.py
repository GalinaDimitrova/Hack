
def number_to_list(n):
    result = []
    while n > 0:
        result.insert(0, n % 10)
        n = n // 10
    return result


def list_to_number(digits):
    result = 0
    lenght = len(digits)
    for i in range(lenght, 0, -1):
        # First we take the first digit and put it in correct place \
        # than we sum it with the other digits
        result += digits[0] * (10 ** (i - 1))
        # We remove used digit to get the other one
        digits.remove(digits[0])
    return result


def zero_insert(n):
    if n < 10:
        print(n)
        return n
    else:
        num_list = number_to_list(n)
        new_num_list = []
        for i in range(len(num_list) - 1):
            if num_list[i] == num_list[i + 1]:
                new_num_list.append(num_list[i])
                new_num_list.append(0)
            elif (num_list[i] + num_list[i + 1]) % 10 == 0:
                new_num_list.append(num_list[i])
                new_num_list.append(0)
            else:
                new_num_list.append(num_list[i])
        new_num_list.append(num_list[len(num_list) - 1])
        num_list = list_to_number(new_num_list)
        print(num_list)
        return num_list


zero_insert(116457)
zero_insert(55555555)
zero_insert(1)
zero_insert(6446)
