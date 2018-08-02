def gen_certain_n_th_digit(n):
    num_of_digit = 1
    num_of_numbers = 9
    base_number = 1

    while n > num_of_digit * num_of_numbers:
        n -= num_of_digit * num_of_numbers
        num_of_digit += 1
        num_of_numbers *= 10
        base_number *= 10

    exact_number = (n - 1) // num_of_digit + base_number
    exact_digit = str(exact_number)[(n - 1) - (n - 1) // num_of_digit * num_of_digit]

    return int(exact_digit)


if __name__ == '__main__':
    ans = 1
    for i in range(7):
        ans *= gen_certain_n_th_digit(pow(10, i))
    print(ans)
