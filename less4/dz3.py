# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

print([l for l in range(20, 240) if l % 20 == 0 or l % 21 == 0])