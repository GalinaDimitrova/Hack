def sevens_in_a_row(arr, n):
	index_first_seven = arr.index(7)
	print(index_first_seven)
	if n == 1:
		print(True)
		return True
	if len(arr) - index_first_seven >= n:
		for j in range(1,n):
			if arr[index_first_seven+j] != 7:
				return sevens_in_a_row(arr[index_first_seven+j+1:],n)
		print(True)
		return True
	else:
		print(False)
		return False




sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3)
sevens_in_a_row([1,7,1,7,7], 4)
sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3)
sevens_in_a_row([7,2,1,6,2], 1)
