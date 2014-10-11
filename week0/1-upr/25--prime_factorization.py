def is_prime(n):
    # we don't check for n == 1 or n < 0 because of the previous \
    # for-loop range
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_factorization(n):
    counter = 0
    result = []
    if is_prime(n) == True:
        result.append((n, 1))
        print(result)
        return result
    # find all primes that could be possible delimeters to "n"
    # 2 is the first prime number
    all_primes = [2]
    # we check only the odd numbers
    for i in range(3, n, 2):
        if is_prime(i) == True:
            all_primes.append(i)
    for item in all_primes:
        while n % item == 0:
            n = n / item
            counter += 1
        if counter > 0:
            result.append((item, counter))
            counter = 0
    print(result)
    return result

prime_factorization(10)
prime_factorization(14)
prime_factorization(356)
prime_factorization(89)
prime_factorization(1000)
