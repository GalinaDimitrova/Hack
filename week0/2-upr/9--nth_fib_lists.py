def nth_fib_lists(listA, listB, n):
    result = []
    if n == 1:
        print(listA)
        return listA
    elif n == 2:
        print(listB)
        return listB
    else:
        for i in range(2, n):
            result = listA + listB
            listA = listB
            listB = result
        print(result)
        return result

nth_fib_lists([1], [2], 1)
nth_fib_lists([1], [2], 2)
nth_fib_lists([1, 2], [1, 3], 3)
nth_fib_lists([], [1, 2, 3], 4)
nth_fib_lists([], [], 100)
