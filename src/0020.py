def cal_sum_of_digits_of_factorial(n):
    inverse_digits_list = [1]

    for num in range(2, n + 1):
        inverse_digits_list = [digit * num for digit in inverse_digits_list]

        for i in range(len(inverse_digits_list) - 1):
            inverse_digits_list[i + 1] += inverse_digits_list[i] // 10
            inverse_digits_list[i] %= 10

        top_digit = inverse_digits_list[-1]
        while top_digit >= 10:
            top_digit = top_digit // 10
            inverse_digits_list[-1] %= 10
            inverse_digits_list.append(top_digit)

    return sum(inverse_digits_list)


if __name__ == '__main__':
    ans = cal_sum_of_digits_of_factorial(100)
    print(ans)
