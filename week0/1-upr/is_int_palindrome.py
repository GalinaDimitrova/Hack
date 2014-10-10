
def revursed(n):
	new_num = 0
	while n > 0:
		new_num += n%10
		new_num = new_num*10
		n = n//10
	new_num = new_num /10
	return new_num


def is_int_palindrome(n):

	if n < 10:
		print(True)
		return True
	else:
		if n == revursed(n):
			print(True)
			return True
	print(False)
	return False


is_int_palindrome(1)
is_int_palindrome(42)
is_int_palindrome(100001)
is_int_palindrome(999)
