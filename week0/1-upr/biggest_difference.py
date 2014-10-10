def biggest_difference(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            result.append(arr[i] - arr[j])
    print(min(result))
    return min(result)

biggest_difference([1, 2])
biggest_difference([1, 2, 3, 4, 5])
biggest_difference([-10, -9, -1])
biggest_difference(range(100))
