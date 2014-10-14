
from collections import Counter


def count_words(arr):
    counts = Counter(arr)
    print(counts)
    return counts


count_words(["apple", "banana", "apple", "pie"])
count_words(["python", "python", "python", "ruby"])
