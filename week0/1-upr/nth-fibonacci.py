def nth_fibonacci(n):
    first = 1
    second = 1
    num = 0
    if n == 1 or n == 2:
        print(1)
        return first
    else:
        for i in range(2,n):
            num = first + second
            first = second
            second = num
        print(num)
        return num

nth_fibonacci(1)
nth_fibonacci(2)
nth_fibonacci(3)
nth_fibonacci(10)


