# Посчитать количество четных элементов в массиве целых чисел, заканчивающихся нулём. Сам ноль учитывать не надо.
# Формат входных данных:
# Массив чисел, заканчивающийся нулём (каждое число с новой строки, ноль не входит в массив)
# Формат выходных данных:
# Одно число — результат.

nums = []
k = None
count = 0
while k != 0:
    k = int(input())
    nums.append(k)
    if k % 2 == 0:
        count += 1
print(count - 1)