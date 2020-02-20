nums = []
n = int(input('Введите количество цифр для сортировки: '))
j = 0
count = 0 #счётчик сравнений
for i in range(n):
    print('Введите любое число №',i+1,':', end=" ")
    nums.append(int(input()))
while j < n-1:
    count += 1
    if nums[j] > nums[j+1]:
        nums[j+1],nums[j] = nums[j],nums[j+1]
        while j > 0:
            count += 1
            if nums[j - 1] > nums[j]:
                nums[j-1],nums[j] = nums[j],nums[j-1]
                j -= 1
            else:
                break
    j += 1

print('Числа отсортированы по возрастанию: ',nums)
print('Минимальное число: ', min(nums))
print('Максимальное число: ', max(nums))
print('Количество проведённых сравнений: ', count)