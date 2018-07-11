def calculate_factors_times(number, current_prime_list, factors_times_dict):
    prime_flag = True

    for prime in current_prime_list:
        if number % prime == 0:
            prime_flag = False
            count = 0
            while number % prime == 0:
                number = number / prime
                count += 1
            if count > factors_times_dict[prime]:
                factors_times_dict[prime] = count
            if number == 1:
                break

    if prime_flag:
        current_prime_list.append(number)
        factors_times_dict[number] = 1

    return


def gen_smallest_evenly_divisible_number(max_division):
    factors_times_dict = {}
    current_prime_list = []
    for i in range(2, max_division + 1):
        calculate_factors_times(i, current_prime_list, factors_times_dict)

    ans = 1
    for factor, times in factors_times_dict.items():
        ans *= pow(factor, times)

    return ans


if __name__ == '__main__':
    ans = gen_smallest_evenly_divisible_number(20)
    print(ans)
