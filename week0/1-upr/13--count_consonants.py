def count_consonants(str):
    counter = 0
    str_len = len(str)
    for i in range(str_len):
        new_str = str.lower()
        if new_str[i] in "bcdfghjklmnpqrstvwxz":
            counter += 1
    print(counter)
    return counter

count_consonants("Python")
count_consonants("Theistareykjarbunga")
count_consonants("grrrrgh!")
count_consonants(
    "Github is the second best thing that happend to programmers, after the keyboard!")
count_consonants("A nice day to code!")
