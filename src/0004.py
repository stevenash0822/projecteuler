# abccba = 11 * (c *100 + b * 910 + a * 9091)


def gen_maximum_palindromic_number():
    for a in range(9, 0, -1):
        for b in range(9, -1, -1):
            for c in range(9, -1, -1):
                second_factor = c *100 + b * 910 + a * 9091
                for div1 in range(10, 91):
                    if second_factor % div1 == 0:
                        div2 = second_factor / div1
                        if (div2 >= 100) and (div2 <= 999):
                            return a * 100001 + b * 10010 + c * 1100


if __name__ == '__main__':
    ans = gen_maximum_palindromic_number()
    print(ans)
