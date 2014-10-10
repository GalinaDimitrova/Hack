def sum_of_digits(n):
	n = abs(n)
	result = 0
	while n > 0:
		result += n%10
		n = n // 10

	print(result)
	return result

sum_of_digits(1325132435356)
sum_of_digits(123)
sum_of_digits(6)
sum_of_digits(-10)
