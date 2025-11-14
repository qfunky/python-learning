numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

odd_indexed_elements = []
for i in range(1, len(numbers), 2):
    odd_indexed_elements.append(numbers[i])

reversed_odd_elements = odd_indexed_elements[::-1]

odd_index_counter = 0
for i in range(1, len(numbers), 2):
    numbers[i] = reversed_odd_elements[odd_index_counter]
    odd_index_counter = odd_index_counter + 1

print("Изменённый список:", numbers)