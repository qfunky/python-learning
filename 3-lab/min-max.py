numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

min_element = numbers[0]
max_element = numbers[0]
min_index = 0
max_index = 0

for i in range(1, len(numbers)):
    if numbers[i] < min_element:
        min_element = numbers[i]
        min_index = i
    if numbers[i] > max_element:
        max_element = numbers[i]
        max_index = i

temp = numbers[min_index]
numbers[min_index] = numbers[max_index]
numbers[max_index] = temp

print("Список с переставленными min и max:", numbers)