def is_prime(n):
    if n < 0:
        print(False)
        return False
    elif n == 1:
        print(False)
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print(False)
                return False
        print(True)
        return True


is_prime(1)  # False
is_prime(2)
is_prime(8)  # False
is_prime(11)
is_prime(-10)  # False
