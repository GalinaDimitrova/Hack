def iterations_of_nan_expand(expanded):
    if expanded == "":
        print(0)
        return 0
    if expanded.count("NaN") == 0:
        print(False)
        return False
    # to check if "Not a " is before "NaN"
    counter = expanded.count("Not a ")
    print(counter)
    return counter





iterations_of_nan_expand("")
iterations_of_nan_expand("Not a NaN")
iterations_of_nan_expand("Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN")
iterations_of_nan_expand("Show these people!")