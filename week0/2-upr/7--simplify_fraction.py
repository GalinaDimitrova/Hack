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


def simplify_fraction(fraction):
    nominator = fraction[0]
    denominator = fraction[1]
    nom_primes = []
    den_primes = []

    if nominator <= denominator and denominator % nominator == 0:
        print((1, denominator // nominator))
        return (1, denominator // nominator)
    elif nominator >= denominator and nominator % denominator == 0:
        print((nominator // denominator, 1))
        return (nominator // denominator, 1)

    if is_prime(nominator):
        nom_primes.append(nominator)
    else:
        # find all primes that could be possible delimeters to "n"
        # 2 is the first prime number
        if nominator % 2 == 0:
            nom_primes.append(2)
        # we check only the odd numbers
        for i in range(3, nominator, 2):
            if is_prime(i) == True:
                if nominator % i == 0:
                    nom_primes.append(i)
    if is_prime(denominator):
        den_primes.append(denominator)
    else:
        # find all primes that could be possible delimeters to "n"
        # 2 is the first prime number
        if denominator % 2 == 0:
            den_primes.append(2)
        # we check only the odd numbers
        for i in range(3, denominator, 2):
            if is_prime(i) == True:
                if denominator % i == 0:
                    den_primes.append(i)
    # now we have all prime delimeters for both numbers
    for i in nom_primes:
        for j in den_primes:
            if i == j:
                nominator = int(nominator / i)
                denominator = int(denominator / i)
    print((nominator, denominator))
    return (nominator, denominator)


simplify_fraction((3, 9))
simplify_fraction((1, 7))
simplify_fraction((4, 10))
simplify_fraction((63, 462))
