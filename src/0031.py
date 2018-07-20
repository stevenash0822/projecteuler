import numpy as np


def dynamic_programming_to_cal_num_of_allocating_ways(coins, total):
    result = np.zeros(total + 1, dtype=int)
    result[0] = 1

    for i in range(coins.shape[0]):
        for money in range(coins[i], total + 1, 1):
            result[money] += result[money - coins[i]]

    return result[total]


if __name__ == '__main__':
    coins_array = np.array([1, 2, 5, 10, 20, 50, 100, 200])
    ans = dynamic_programming_to_cal_num_of_allocating_ways(coins_array, 200)
    print(ans)
