# task 1
SEC_IN_MIN = 60
SEC_IN_HOUR = 60 * 60
SEC_IN_DAY = 60 * 60 * 24

# duration in seconds
def print_datetime(duration):
    duration_str = ""
    # days
    duration_days = duration // SEC_IN_DAY
    if duration_days > 0:
        duration_str = duration_str + str(duration_days) + " дн."
    duration = duration % SEC_IN_DAY
    # hours
    duration_hours = duration // SEC_IN_HOUR
    if duration_hours > 0 or duration_days > 0:
        duration_str = duration_str + str(duration_hours) + " час "
    duration = duration % SEC_IN_HOUR
    # mins
    duration_mins = duration // SEC_IN_MIN
    if duration_mins > 0 or duration_hours > 0 or duration_days > 0:
        duration_str = duration_str + str(duration_mins) + " мин "
    duration = duration % SEC_IN_MIN
    # sec
    duration_str = duration_str + str(duration) + " сек "
    print(duration_str)

# task 2
def summ_numbers_eq7(l_in):
    summ = 0
    for l_elem in l_in:
        sum_letters = 0
        for l_letter in str(l_elem):
            sum_letters += int(l_letter)
        if sum_letters % 7 == 0:
            summ = summ + l_elem
    return summ

# list of cubed numbers
def create_list_cubed_numbers(min_val, max_val):
    l_numbers = []
    for i in range (min_val, max_val):
        l_numbers.append(i**3)
    summ = summ_numbers_eq7(l_numbers)
    print(summ)
    # в задании не понятно к какому списку нужно добавить 17
    # к результирующему, полученному из тех, сумма цифр кот. делится
    # на 7 или к исходному полученному.
    for l_elem in l_numbers:
        l_elem += 17
    summ = summ_numbers_eq7(l_numbers)
    print(summ)

# task 3
def procents_plural_form(number):
    number = number % 100
    if number > 10 and number < 20:
        return "процентов"
    if number % 10 > 1 and number % 10 < 5:
        return "процента"
    if number % 10 == 1:
        return "процент"
    return "процентов"

def crate_list_procents(min_val, max_val):
    for i in range(min_val, max_val):
        print(i, " ", procents_plural_form(i))


if __name__ == '__main__':
    print_datetime(4153)
    create_list_cubed_numbers(1, 1000)
    crate_list_procents(1, 100)