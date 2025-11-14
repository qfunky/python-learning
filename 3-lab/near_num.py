numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
x = int(input("Введите число x: "))

closest_number = numbers[0]
min_difference = abs(x - closest_number)

for number in numbers:
    difference = abs(x - number)
    if difference < min_difference:
        min_difference = difference
        closest_number = number

print("Ближайшее число:", closest_number)