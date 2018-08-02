# Assume a^2 + b^2 = c^2 with a <= b < c. And p = a + b + c
# Then a <= trunc(p / (1 + 1 + sqrt(2)))
# As a^2 = (c + b)(c - b),
# So just traverse a, to ensure that (c + b) and (c - b) have the same parity and (c + b) - (c - b) >= 2 * a.
# And use constraint c + b >= ceil(a * (1 + sqrt(2))) to decrease the search scope.

# However, in this program, we just use simple search strategy.


import time
import math
import numpy as np


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Total running time of Function %s(): %.4f seconds" % (func.__name__, end - start))
        return result

    return wrapper


@timeit
def gen_perimeter_of_right_angle_triangle_with_maximum_integral_solution(upper_bound):
    perimeter_solution_array = np.zeros(upper_bound + 1, dtype=int)

    for a in range(3, math.trunc(upper_bound / (1 + 1 + math.sqrt(2)))):
        for b in range(a, (upper_bound - a) // 2 + 1):
            c = math.sqrt(a ** 2 + b ** 2)
            p = a + b + int(c)
            if p > upper_bound:
                break
            if c - int(c) == 0:
                perimeter_solution_array[p] += 1

    return np.argmax(perimeter_solution_array)


if __name__ == '__main__':
    ans = gen_perimeter_of_right_angle_triangle_with_maximum_integral_solution(1000)
    print(ans)
