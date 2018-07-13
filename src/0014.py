def cal_length_chain(number, number_length_dict):
    if number == 1:
        return 1
    elif number in number_length_dict.keys():
        return number_length_dict[number]
    else:
        if number % 2 == 0:
            number_length_dict[number] = cal_length_chain(number // 2, number_length_dict) + 1
            return number_length_dict[number]
        else:
            number_length_dict[number] = cal_length_chain(number * 3 + 1, number_length_dict) + 1
            return number_length_dict[number]


def gen_number_owns_longest_chain(upper_bound):
    number_length_dict = {1:1}
    maximum_length = 0
    maximum_cor_number = 0

    for i in range(2, upper_bound):
        length = cal_length_chain(i, number_length_dict)
        if length > maximum_length:
            maximum_length = length
            maximum_cor_number = i

    return maximum_cor_number


if __name__ == '__main__':
    ans = gen_number_owns_longest_chain(1000000)
    print(ans)