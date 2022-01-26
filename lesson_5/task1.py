# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield:

def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield num

gener = odd_nums(11)

# test
# for i in range(0, 12):
#     print(i, next(gener), sep = ' - ')

