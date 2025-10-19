# Анализатор надежности пароля с расширенными проверками

import re

def analyze_password_final(password):
    score = 0
    details = []
    recommendations = []
    length = len(password)

    if length < 8:
        details.append("Длина: < 8 символов (очень плохо)")
        recommendations.append("Увеличить длину до 12+ символов")
    elif 8 <= length <= 12:
        score += 1
        details.append("Длина: 8-12 символов (хорошо)")
    else:
        score += 2
        details.append("Длина: > 12 символов (отлично)")

    if re.search(r"\d", password):
        score += 1
        details.append("Цифры: есть (хорошо)")
    else:
        details.append("Цифры: нет (плохо)")
        recommendations.append("Добавить цифры")
    if re.search(r"[A-ZА-Я]", password):
        score += 1
        details.append("Заглавные буквы: есть (хорошо)")
    else:
        details.append("Заглавные буквы: нет (плохо)")
        recommendations.append("Добавить заглавные буквы")
    if re.search(r"[a-zа-я]", password):
        score += 1
        details.append("Строчные буквы: есть (хорошо)")
    else:
        details.append("Строчные буквы: нет (плохо)")
        recommendations.append("Добавить строчные буквы")
    if re.search(r"[!@#$%^&*(),.?\"\':{}|<>]", password):
        score += 1
        details.append("Спецсимволы: есть (хорошо)")
    else:
        details.append("Спецсимволы: нет (плохо)")
        recommendations.append("Добавить специальные символы")
        sequences = ["123", "234", "qwe", "wer", "asd", "sdf", "zxc", "йцу", "фыв", "ячс"]
        
    if not any(seq in password.lower() for seq in sequences):
        score += 1
        details.append("Последовательности: не найдены (хорошо)")
    else:
        details.append("Последовательности: найдены (плохо)")
        recommendations.append("Избегать очевидных последовательностей")
        popular_passwords = ["123456", "password", "123456789", "qwerty", "пароль"]
    if password.lower() in popular_passwords:
        score = 0
        details.append("Популярность: пароль слишком известен (критично)")
        recommendations.append("Использовать уникальный пароль")
    if re.search(r"(.)\1{2,}", password):
        score -= 2
        details.append("Повторы символов: есть (плохо)")
        recommendations.append("Избегать повторения символов подряд")
    if password.isdigit() or password.isalpha():
        score -= 2
        details.append("Шаблон: только буквы или только цифры (плохо)")
        recommendations.append("Комбинировать разные типы символов")
        score = max(0, score)

    if score <= 2:
        level = "Очень слабый"
    elif score <= 4:
        level = "Слабый"
    elif score <= 6:
        level = "Средний"
    elif score <= 7:
        level = "Сильный"
    else: 
        level = "Очень сильный"
    print("\n--- Результат анализа ---")
    print(f"Оценка: {score}/8 | Уровень: {level}")
    print("\nДетали:")
    for d in details:
        print(f" - {d}")
    if recommendations:
        print("\nРекомендации:")
    for r in recommendations:
        print(f" - {r}")

password_input = input("Введите пароль для анализа: ")
analyze_password_final(password_input)