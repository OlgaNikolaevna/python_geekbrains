# Есть два списка: tutors ,  klasses
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>),
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде:  (<tutor>, None)
### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях генератор даст эффект.
import itertools

tutors = [
    'Иван', 'Анастасия', 'Петр'
]

klasses = [
    '9А', '7В'
]
gen_tutor_classes =  tuple()
gen_tutor_classes = ((tut, kl) for tut, kl in itertools.zip_longest(tutors, klasses) if tut)

print(type(gen_tutor_classes)) # это генератор

print(next(gen_tutor_classes))
print(next(gen_tutor_classes))
print(next(gen_tutor_classes))

print(next(gen_tutor_classes)) # StopIteration

# Подумать, в каких ситуациях генератор даст эффект:
# Возможно чтобы разово вывести данные указанного вида (условно печать). Или в задачах поиска оптимальных расписаний для минимизации объема используемой ОП