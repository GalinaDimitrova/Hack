def is_increasing(seq):
    if len(seq) == 1:
        print(True)
        return True
    # len(seq)-1 -- otherwise it will get out of range in seq[last +1]
    for i in range(len(seq) - 1):
        if seq[i] >= seq[i + 1]:
            print(False)
            return False
    print(True)
    return True


is_increasing([1, 2, 3, 4, 5])
is_increasing([1])
is_increasing([5, 6, -10])
is_increasing([1, 1, 1, 1])
