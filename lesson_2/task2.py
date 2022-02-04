# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
L_AUXIL_SYMBOLS =['+','-']

l_phrase = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
l_result = []
for phrase_word in l_phrase:
    phrase_word_nosign = phrase_word.replace('+', '')
    if phrase_word_nosign.isnumeric():
        l_result.append('"')
        res_word = phrase_word
        if (len(phrase_word_nosign)) < 2:
            if (len(phrase_word_nosign)) == len(phrase_word):
                res_word = '0' + phrase_word_nosign
            else:
                res_word = '+' + '0' + phrase_word_nosign
        l_result.append(res_word)
        l_result.append('"')
    else:
        l_result.append(phrase_word)

print(l_result)