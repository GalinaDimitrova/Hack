def groupby(func, seq):
    result = {}
    for item in seq:
        key = func(item)
        if key in result:
            result[key].append(item)
        else:
            result[key] = [item]
    print(result)
    return result


groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7])
groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12])
groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7])
