def member_of_nth_fib_lists(listA, listB, needle):
    new_list = []
    if listA == needle or listB == needle:
        print(True)
        return True
    else:
        while len(new_list) < len(needle):
            new_list = listA + listB
            listA = listB
            listB = new_list
        if len(new_list) == len(needle):
            if new_list == needle:
                print(True)
                return True
        else:
            print(False)
            return False

member_of_nth_fib_lists([1, 2], [3, 4], [5, 6])
member_of_nth_fib_lists([1, 2], [3, 4], [1, 2, 3, 4, 3, 4, 1, 2, 3, 4])
member_of_nth_fib_lists([7, 11], [2], [7, 11, 2, 2, 7, 11, 2])
member_of_nth_fib_lists([7, 11], [2], [11, 7, 2, 2, 7])
