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
    return result
