def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
            else:
                i += 1
        return True


def prime_possible_delimeters(number):
    list_of_primes = []
    if is_prime(number):
        list_of_primes.append(number)
    else:
        # find all primes that could be possible delimeters to "n"
        # 2 is the first prime number
        if number % 2 == 0:
            list_of_primes.append(2)
        # we check only the odd numbers
        for i in range(3, number, 2):
            if is_prime(i) == True:
                if number % i == 0:
                    list_of_primes.append(i)
    return list_of_primes


def simplify_fraction(fraction):
    nominator = fraction[0]
    denominator = fraction[1]
    nom_primes = []
    den_primes = []

    if nominator <= denominator and denominator % nominator == 0:
        return (1, denominator // nominator)
    elif nominator >= denominator and nominator % denominator == 0:
        return (nominator // denominator, 1)

    nom_primes = prime_possible_delimeters(nominator)
    den_primes = prime_possible_delimeters(denominator)
    # now we have all prime delimeters for both numbers
    for i in nom_primes:
        for j in den_primes:
            if i == j:
                nominator = int(nominator / i)
                denominator = int(denominator / i)
    return (nominator, denominator)
