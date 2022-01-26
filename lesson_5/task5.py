# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
from time import perf_counter
import random

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#src = [random.randint(1, 100) for _ in range(100)]

# в лоб
t_st = perf_counter()
result = [el for el in src if src.count(el) == 1]
#print(result)
print(' Duration 1 = ', perf_counter() - t_st)
# не в лоб. Хэш табл.
t_st = perf_counter()
unique_src = set()
tmp = set()
for num in src:
   if num not in tmp:
       unique_src.add(num)
   else:
       unique_src.discard(num)
   tmp.add(num)

result = [num for num in src if num in unique_src]
#print(result)
print(' Duration 2= ', perf_counter() - t_st)

# Если число эл-в 100:
#   Duration 1=  0.00012860004790127277
#   Duration 2=  3.4800032153725624e-05
# Если число эл-в 1000:
#   Duration 1= 0.013514099875465035
#   Duration 2= 0.0003217000048607588
# Если число эл-в 10000:
#   Duration 1 = 1.209448000183329
#   Duration 2 = 0.002394299954175949

