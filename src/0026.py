def cal_recurring_cycles(denominator):
    remainder_list = []
    current_remainder = 1

    while True:
        current_remainder %= denominator

        if current_remainder == 0:
            return 0

        if current_remainder not in remainder_list:
            remainder_list.append(current_remainder)
            current_remainder *= 10
        else:
            return len(remainder_list) - remainder_list.index(current_remainder)


def cal_denominator_with_longest_recurring_cycle(upper_bound):
    maximum_length = 0
    maximum_cor_denominator = 0

    for i in range(2, upper_bound):
        length = cal_recurring_cycles(i)
        if length > maximum_length:
            maximum_length = length
            maximum_cor_denominator = i

    return maximum_cor_denominator


if __name__ == '__main__':
    ans = cal_denominator_with_longest_recurring_cycle(1000)
    print(ans)
