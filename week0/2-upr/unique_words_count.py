def unique_words_count(arr):
    unique_words = set(arr)
    counter = 0
    for i in unique_words:
        counter += 1

    return counter

# unique_words_count(["apple", "banana", "apple", "pie"])
# unique_words_count(["python", "python", "python", "ruby"])
# unique_words_count(["HELLO!"] * 10)
