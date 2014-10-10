def sum_of_divisors(n):
	num = 0
	for i in range(1,n+1):
		if n % i == 0:
			num += i
	print(num)
	return num


sum_of_divisors(8)
sum_of_divisors(7)
sum_of_divisors(1)
sum_of_divisors(1000)
