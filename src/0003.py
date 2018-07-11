def judge_prime(number, current_prime_list):
    for prime in current_prime_list:
        if number % prime == 0:
            return False
    current_prime_list.append(number)
    return True


def gen_maximum_prime_factor(query):
    current_prime_list = []
    current_factor = 2
    while current_factor <= query:
        if judge_prime(current_factor, current_prime_list):
            while query % current_factor == 0:
                query = query / current_factor
            if query == 1:
                return current_factor
        current_factor += 1


if __name__ == '__main__':
    ans = gen_maximum_prime_factor(600851475143)
    print(ans)
