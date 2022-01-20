# 2. Написать функцию (), принимающую в качестве аргумента код валюты (например, , EUR, , ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

from requests import get, utils
import xml.etree.ElementTree as ET


def get_exchange_rate (currency_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    currency_code = currency_code.upper()
    content = response.content.decode(encoding=response.encoding)
    root = ET.fromstring(content)
    val = None
    for i in range(0, len(root)):
        char_code = root[i][1].text
        if char_code == currency_code:
            val = float(root[i][4].text.replace(',', '.'))
    return val


def call_test():
    print(type(('USD')))
    print(get_exchange_rate('USD'))
    print(get_exchange_rate('usd'))
    print(get_exchange_rate('GBP'))
    print(get_exchange_rate('USD1'))


if __name__ == '__main__':
    call_test()