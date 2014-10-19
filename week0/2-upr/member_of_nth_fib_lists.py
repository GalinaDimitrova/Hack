def member_of_nth_fib_lists(listA, listB, needle):
    new_list = []
    if listA == needle or listB == needle:
        return True
    else:
        while len(new_list) < len(needle):
            new_list = listA + listB
            listA = listB
            listB = new_list
        if len(new_list) == len(needle):
            if new_list == needle:
                return True
        else:
            return False
