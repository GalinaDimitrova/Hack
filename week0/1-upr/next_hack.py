
def reverse_string(str1):
    result = []
    for letter in str1:
        result.insert(0, letter)
    return str("".join(result))


def is_palindrome(str1):
    count = len(str1)
    if count == 1:
        return True
    for i in range(0, count // 2 + 1):
        if(str1[i] != str1[count - i - 1]):
            return False
    return True


def convert_to_binary(n):
    bin_num = ""
    if n == 0:
        bin_num = "0"
    while n > 0:
        if n % 2 == 0:
            bin_num += str(n % 2)
            n = n // 2
        else:
            bin_num = bin_num + str(n % 2)
            n = n // 2
            # Reverse the string
    bin_num = reverse_string(bin_num)
    return bin_num


def is_hack(bin_num):
    if bin_num.count("1") % 2 != 0 and is_palindrome(bin_num):
        return True
    else:
        return False


def next_hack(n):
    # It should start from the next element
    bin_num = ""
    bin_num = convert_to_binary(n + 1)
    if is_hack(bin_num) != True:
        return next_hack(n + 1)
    print(n + 1)
    return n + 1

next_hack(0)
next_hack(10)
next_hack(8031)
