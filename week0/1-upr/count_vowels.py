def count_vowels(str):
    counter = 0
    str_len = len(str)
    for i in range(str_len):
        new_str = str.lower()
        if new_str[i] in "aeiouy":
            counter += 1
    print(counter)
    return counter

count_vowels("Python")
count_vowels("Theistareykjarbunga") #It's a volcano name!
count_vowels("grrrrgh!")
count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")
count_vowels("A nice day to code!")