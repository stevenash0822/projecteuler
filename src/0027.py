# when n = 0, b must be a prime
# when n = 1, a must be an odd


import math


def judge_prime(number):
    if number <= 1:
        return False

    for i in range(2, math.trunc(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def cal_product_of_a_b_under_maximum_number_of_consecutive_primes():
    possible_values_for_a_list = [a for a in range(-999, 1000) if a % 2 == 1]
    possible_values_for_b_list = [b for b in range(1001) if judge_prime(b)]

    maximum_number_of_consecutive_primes = 0
    maximum_cor_a, maximum_cor_b = 0, 0
    for a in possible_values_for_a_list:
        for b in possible_values_for_b_list:
            n = 1
            number_of_consecutive_primes = 1
            while judge_prime(n * n + a * n + b):
                number_of_consecutive_primes += 1
                n += 1

            if number_of_consecutive_primes > maximum_number_of_consecutive_primes:
                maximum_number_of_consecutive_primes = number_of_consecutive_primes
                maximum_cor_a = a
                maximum_cor_b = b

    return (maximum_cor_a * maximum_cor_b)


if __name__ == '__main__':
    ans = cal_product_of_a_b_under_maximum_number_of_consecutive_primes()
    print(ans)
