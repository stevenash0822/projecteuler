# The sequence of triangle numbers has the forms as below:
#   m * (2m - 1), m * (2m + 1), ...  {m >= 1, m is int}


import math


def gen_factors_set(number):
    result = set()

    for i in range(1, math.trunc(math.sqrt(number)) + 1):
        if number % i == 0:
            result.add(i)
            result.add(number // i)

    return result


def cal_factors_num(mul1, mul2, number_factors_dict):
    if mul1 not in number_factors_dict.keys():
        number_factors_dict[mul1] = gen_factors_set(mul1)
    if mul2 not in number_factors_dict.keys():
        number_factors_dict[mul2] = gen_factors_set(mul2)

    # generate factors (1 <= factor <= mul1) of mul1 * mul2
    temp_set1 = number_factors_dict[mul1] | number_factors_dict[mul2]
    temp_set1.remove(mul2)

    # generate factors (mul1 < factor <= trunc(sqrt(mul1 * mul2))) of mul1 * mul2
    upper_bound_fac = math.trunc(math.sqrt(mul1 * mul2))
    temp_set2 = {i * j for i in number_factors_dict[mul1]
                 for j in number_factors_dict[mul2]
                 if (i * j not in temp_set1) and (i * j <= upper_bound_fac)}

    if math.sqrt(mul1 * mul2) - upper_bound_fac == 0:
        return (len(temp_set1) + len(temp_set2)) * 2 - 1
    else:
        return (len(temp_set1) + len(temp_set2)) * 2


def gen_triangle_number(lower_bound_factors_num):
    m = 1
    number_factors_dict = {}
    cal_factors_num(8, 15, number_factors_dict)

    while True:
        # deal with m * (2m - 1)
        if cal_factors_num(m, 2 * m - 1, number_factors_dict) > lower_bound_factors_num:
            return m * (2 * m - 1)

        # deal with m * (2m + 1)
        if cal_factors_num(m, 2 * m + 1, number_factors_dict) > lower_bound_factors_num:
            return m * (2 * m + 1)

        m += 1


if __name__ == '__main__':
    ans = gen_triangle_number(500)
    print(ans)
