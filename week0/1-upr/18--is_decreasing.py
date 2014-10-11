def is_decreasing(seq):
    if len(seq) == 1:
        print(True)
        return True
    # len(seq)-1 -- otherwise it will get out of range in seq[last +1]
    for i in range(len(seq) - 1):
        if seq[i] <= seq[i + 1]:
            print(False)
            return False
    print(True)
    return True


is_decreasing([5, 4, 3, 2, 1])
is_decreasing([1, 2, 3])
is_decreasing([100, 50, 20])
is_decreasing([1, 1, 1, 1])
