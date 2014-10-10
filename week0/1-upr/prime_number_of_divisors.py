def is_prime(n):
	if n < 0:
		return False
	elif n == 1:
		return False
	else:
		for i in range(2,int(n**0.5)+1):
			if n % i == 0:
				return False
			else:
				i += 1
		return True


def prime_number_of_divisors(n):
	
	for i in range(2, n):
		if n % i == 0:
			if is_prime(i) == False:
				print(False)
				return False
			else:
				i += 1
	print(True)
	return True

prime_number_of_divisors(7)
prime_number_of_divisors(8)
prime_number_of_divisors(9)




