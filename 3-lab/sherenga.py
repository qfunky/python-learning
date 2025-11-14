heights = list(map(int, input("Введите росты учеников через пробел: ").split()))
petya_height = int(input("Введите рост Пети: "))

position = 1

for height in heights:
    if petya_height <= height:
        position = position + 1
    else:
        break

print("Номер Пети в строю:", position)