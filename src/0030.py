from functools import reduce


def cal_sum_of_fifth_powers_equivalent_numbers():
    result = 0

    for number in range(2, 1000000):
        iterator_list = list(str(number))
        if number == reduce(lambda x, y: x + y, map(lambda x: pow(int(x), 5), iterator_list)):
            result += number

    return result


if __name__ == '__main__':
    ans = cal_sum_of_fifth_powers_equivalent_numbers()
    print(ans)
