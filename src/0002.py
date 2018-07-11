def fib(upper_bound):
    a, b = 0, 1
    while b < upper_bound:
        yield b
        a, b = b, a+b
    return


if __name__ == '__main__':
    total = 0
    for i in fib(4000000):
        if i % 2 == 0:
            total += i
    print(total)
