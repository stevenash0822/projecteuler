# We use 0~6 to represent Sunday~Saturday


def cal_sum_of_lucky_sunday(start_year, start_month, end_year, end_month, initial_date):
    month_dates_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    day = initial_date
    count = 0

    for year in range(start_year, end_year + 1):
        if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
            month_dates_dict[2] = 29
        else:
            month_dates_dict[2] = 28

        for month in range(start_month if year == start_year else 1,
                           end_month + 1 if year == end_year else 13):
            if day == 0:
                count += 1
            day += month_dates_dict[month]
            day %= 7

    return count


if __name__ == '__main__':
    ans = cal_sum_of_lucky_sunday(1901, 1, 2000, 12, 2)
    print(ans)
