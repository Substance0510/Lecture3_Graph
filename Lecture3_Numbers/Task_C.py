# Требуется определить, является ли данный год високосным. (Год является високосным, если его номер кратен 4,
# но не кратен 100, а также если он кратен 400).
# Формат входных данных:
# На вход подается натуральное число N - номер года (0 < N < 100000).
# Формат выходных данных:
# Вывести YES если год високосный и NO в противном случае.

N = int(input())
while True:
    if N <= 0:
        print('Please, enter a number of year between 0 - 100000')
        N = int(input())
    elif N > 100000:
        print('Please, enter a number of year between 0 - 100000')
        N = int(input())
    else:
        break
if N % 4 == 0:
    if N % 400 == 0:
        print('YES')
    elif N % 100 == 0:
        print('NO')
    else:
        print('YES')
elif N % 400 == 0:
    print('YES')
else:
    print('NO')