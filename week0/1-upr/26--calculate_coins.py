def calculate_coins(sum):
    sum = sum * 100
    list_of_coins = [100, 50, 20, 10, 5, 2, 1]
    coin_counter = 0
    result_dict = {}
    for i in list_of_coins:
        if sum - i < 0:
            result_dict[i] = coin_counter
        else:
            while sum - i >= 0:
                sum -= i
                coin_counter += 1
            result_dict[i] = coin_counter
            coin_counter = 0
    print(result_dict)

calculate_coins(0.53)
calculate_coins(8.94)
