# Написать функцию num_translate(), переводящую числительные от 0 до 10
# c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше
# хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
dict_numerics = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'tree': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

def num_translate(num_eng):
    """translate numerics from ENG to RUS"""
    num_eng = num_eng.lower()
    num_rus = dict_numerics.get(num_eng, None)
    return num_rus


print(num_translate("eight"))
print(num_translate("ten"))
print(num_translate("eleven"))