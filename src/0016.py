def cal_sum_of_digits_of_pow2(power):
    inverse_digits_list = [1]

    for num in range(power):
        inverse_digits_list = [digit*2 for digit in inverse_digits_list]
        for i in range(len(inverse_digits_list) - 1):
            inverse_digits_list[i + 1] += inverse_digits_list[i] // 10
            inverse_digits_list[i] %= 10
        if inverse_digits_list[-1] >= 10:
            top_digit = inverse_digits_list[-1] // 10
            inverse_digits_list[-1] %= 10
            inverse_digits_list.append(top_digit)

    return sum(inverse_digits_list)


if __name__ == '__main__':
    ans = cal_sum_of_digits_of_pow2(1000)
    print(ans)
