# ===== Задание 1: Ближайшее число, кратное 13 =====
N = int(input())
while N % 13 != 0:
    N += 1
print(N)


# ===== Задание 2: Второй минимум последовательности =====
min1 = None
min2 = None

while True:
    x = int(input())
    if x == 0:
        break

    if min1 is None:
        min1 = x
    elif min2 is None:
        if x < min1:
            min2 = min1
            min1 = x
        else:
            min2 = x
    else:
        if x < min1:
            min2 = min1
            min1 = x
        elif x < min2:
            min2 = x

print(min2)



# ===== Задание 3: Количество локальных максимумов =====
count = 0
prev = int(input())
curr = int(input())

while curr != 0:
    next_val = int(input())
    if next_val == 0:
        break
    if curr > prev and curr > next_val:
        count += 1
    prev, curr = curr, next_val

print(f'Количество лок максимумов: {count}')


# ===== Задание 4: Вычисление выражения из строки =====
s = input()
result = int(s[0])

for i in range(1, len(s), 2):
    operator = s[i]
    number = int(s[i + 1])
    if operator == '+':
        result += number
    elif operator == '-':
        result -= number

print(result)


# ===== Задание 5: Самая длинная подстрока с одинаковыми краями =====
def solve_problem(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""

    max_length = 0
    longest_substring = ""

    for i in range(n):
        for j in range(n - 1, i - 1, -1):
            if s[i] == s[j]:
                current_length = j - i + 1
                if current_length > max_length:
                    max_length = current_length
                    longest_substring = s[i:j + 1]
                break
        if n - i <= max_length:
            break

    if not longest_substring and n > 0:
        return s[0]

    return longest_substring


print(solve_problem("nhegabracadabrawrher"))


# ===== Задание 6: Вставка '*' между символами =====
original_string = input()
new_string = '*'.join(original_string)
print(new_string)


# ===== Задание 7: Замена 'h' между первой и последней =====
s = input()
try:
    first_h = s.index('h')
    last_h = s.rindex('h')
except ValueError:
    print(s)
    exit()

if first_h == last_h:
    print(s)
    exit()

middle = s[first_h + 1:last_h].replace('h', 'H')
result = s[:first_h + 1] + middle + s[last_h:]
print(result)
