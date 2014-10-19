def is_prime(n):
    # we don't check for n == 1 or n < 0 because of the previous \
    # for-loop range
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def goldbach(n):
    result = []
    all_primes = [2]
    # we check only the odd numbers
    for i in range(3, n, 2):
        if is_prime(i) == True:
            all_primes.append(i)
    for i in range(len(all_primes)):
        for j in range(len(all_primes) - 1, -1, -1):
            if all_primes[i] + all_primes[j] == n:
                result.append((all_primes[i], all_primes[j]))
                break
    if len(result) > 1:
        # removing duplicate  tuples
        for (x, y) in result:
            if x != y:
                result.remove((y, x))
    return result


