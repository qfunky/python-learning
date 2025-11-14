numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

last_element = numbers[len(numbers) - 1]

for i in range(len(numbers) - 2, -1, -1):
    numbers[i + 1] = numbers[i]

numbers[0] = last_element

print("Результат сдвига:", numbers)