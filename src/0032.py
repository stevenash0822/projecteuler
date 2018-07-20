# By inference, the multiplicand/multiplier/product pairs must be 4/1/4 digits or 3/2/3 digits
# (suppose multiplicand >= multiplier)


from itertools import permutations


def judge_pandigital(digit_sequence):
    product = digit_sequence[5] * 1000 + digit_sequence[6] * 100 + digit_sequence[7] * 10 + digit_sequence[8]

    multiplicand = digit_sequence[0] * 1000 + digit_sequence[1] * 100 + digit_sequence[2] * 10 + digit_sequence[3]
    multiplier = digit_sequence[4]
    if multiplicand * multiplier == product:
        return product

    multiplicand = digit_sequence[0] * 100 + digit_sequence[1] * 10 + digit_sequence[2]
    multiplier = digit_sequence[3] * 10 + digit_sequence[4]
    if multiplicand * multiplier == product:
        return product

    return 0


def cal_sum_of_all_pandigital_products():
    pandigital_product_set = set()

    digit_sequence_list = list(permutations(range(1, 10), 9))
    for digit_sequence in digit_sequence_list:
        effective_product = judge_pandigital(digit_sequence)
        if effective_product:
            pandigital_product_set.add(effective_product)

    return sum(pandigital_product_set)


if __name__ == '__main__':
    ans = cal_sum_of_all_pandigital_products()
    print(ans)
