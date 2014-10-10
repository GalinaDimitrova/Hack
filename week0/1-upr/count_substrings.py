def count_substrings(haystack, needle):
    counter = haystack.count(needle)
    print(counter)
    return counter

count_substrings("This is a test string", "is")
count_substrings("babababa", "baba")
count_substrings("Python is an awesome language to program in!", "o")
count_substrings("We have nothing in common!", "really?")
count_substrings("This is this and that is this", "this")  # "This" != "this"