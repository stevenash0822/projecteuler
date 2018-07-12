# Assume that a <= b < c, all int
# a^2 + b^2 = c^2, a + b + c = sum
# Inference1: a <= math.floor(sum / (1 + 1 + math.sqrt(2)))
# Inference2: assert c - b = a^2 / (sum - a) is int


def gen_pythagorean_triplet(sum_value):
    import math

    for a in range(1, int(math.floor(sum_value / (1 + 1 + math.sqrt(2)))) + 1):
        if (a * a) % (sum_value - a) == 0:
            c = ((sum_value - a) + (a * a) // (sum_value - a)) // 2
            b = sum_value - a - c
            return a, b, c

    return 0, 0, 0


if __name__ == '__main__':
    a, b, c = gen_pythagorean_triplet(1000)
    print(a * b * c)

