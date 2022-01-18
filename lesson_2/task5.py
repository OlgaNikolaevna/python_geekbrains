# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

l_prices = [57.8, 46.51, 97, 11, 145, 11, 7, 587, 41, 57.1, 10]
l_prices_copy = l_prices.copy()
l_prices_formated = []

def show_formated_prices(l_pr):
    res_str = ""
    for pr in l_pr:
        res = str(pr).split(".", 1)
        if len(res) < 2:
            pr_k = 0
        else:
            pr_k = res.pop()
        pr_r = res.pop()
        pr_formated = '{0} руб {1:02} коп'.format(pr_r, pr_k)
        if res_str == "":
            res_str = pr_formated
        else:
            res_str = res_str + ", " + pr_formated
    print(res_str)


show_formated_prices(l_prices)
id_before = id(l_prices)

l_prices.sort()
show_formated_prices(l_prices)
id_after = id(l_prices)
if id_before == id_after:
    print("Объект тот же")
else:
    print("Объект поменятся. Но этого не произойдет")

l_prices_sort = sorted(l_prices, reverse = True)
show_formated_prices(l_prices_sort)

