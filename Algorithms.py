def get_evens(numbers):
    return [x for x in numbers if x % 2 == 0]

def find_max(numbers):
    max_num = numbers[0]
    for x in numbers:
        if x > max_num:
            max_num = x
    return max_num

def find_min(numbers):
    min_num = numbers[0]
    for x in numbers:
        if x < min_num:
            min_num = x
    return min_num

def bubble_sort(numbers):
    nums = numbers.copy()
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# Основная часть
input_numbers = [int(x) for x in input("Введите числа через запятую: ").split(',')]

print("Чётные числа:", get_evens(input_numbers))
print("Максимальное число:", find_max(input_numbers))
print("Минимальное число:", find_min(input_numbers))
print("Отсортированный список:", bubble_sort(input_numbers))