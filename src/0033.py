from functools import reduce


def gcd(m, n):
    if m < n:
        m, n = n, m

    while m % n:
        m, n = n, m % n

    return n


def cal_denominator_of_product_of_all_curious_fractions_in_lowest_common_terms():
    curious_fraction_numerator_list = []
    curious_fraction_denominator_list = []

    for a in range(10, 99):
        for b in range(a+1, 100):
            if a % 10 == b // 10:
                if (a // 10) * b == (b % 10) * a:
                    curious_fraction_numerator_list.append(a)
                    curious_fraction_denominator_list.append(b)

    numerator = reduce(lambda x, y: x * y, curious_fraction_numerator_list)
    denominator = reduce(lambda x, y: x * y, curious_fraction_denominator_list)

    denominator = denominator // gcd(numerator, denominator)

    return denominator


if __name__ == '__main__':
    ans = cal_denominator_of_product_of_all_curious_fractions_in_lowest_common_terms()
    print(ans)
