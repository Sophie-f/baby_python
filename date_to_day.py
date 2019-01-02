def make_day(my_date):
    month_dict = {'March': 1, 'April': 2, ' May': 3, 'June': 4, 'July': 5, 'August': 6, 'September': 7, 'October': 8,
                  'November': 9, 'December': 10, 'January': 11, 'February': 12}

    day_dict = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    my_date = my_date.split()
    day = int(my_date[1])
    mount = month_dict[my_date[0]]
    year = int(my_date[2])
    century = year // 100
    year = year - century * 100
    x = (day + int(2.6 * mount - 0.2) - 2 * century + year + (year // 4) + century // 4) % 7
    return day_dict[x]


print(make_day(input('enter the date like (May 5 1992)')))
