def sort_fractions(fractions):
    fraction_dict = {}
    to_sort_list = []
    result = []
    for item in fractions:
        num = item[0] / item[1]
        fraction_dict[num] = item
        to_sort_list.append(num)

    to_sort_list.sort()
    for i in to_sort_list:
        result.append((fraction_dict[i]))
    print(result)
    return result


sort_fractions([(2, 3), (1, 2)])
sort_fractions([(2, 3), (1, 2), (1, 3)])
sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)])
