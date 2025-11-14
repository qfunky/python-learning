numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
pair_count = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            pair_count = pair_count + 1

print("Количество совпадающих пар:", pair_count)