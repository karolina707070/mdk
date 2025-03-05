from number_operations import NumberProcessor # Импортируем класс NumberProcessor из модуля number_operations.
from number_transformer import power, transform_with_map, filter_with_lambda # Импортируем функции power, transform_with_map и filter_with_lambda из модуля number_transformer.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Создаем список чисел.
processor = NumberProcessor(numbers) # Создаем объект NumberProcessor, передавая ему список чисел.

# Демонстрация методов NumberProcessor 
prime_numbers = processor.fil(processor.is_prime) # Используем метод fil для фильтрации списка чисел, оставляя только простые числа (используя метод is_prime).
print(f"Простые числа: {prime_numbers}")  # Выводим список простых чисел.

factorial_of_5 = processor.factorial(5) # Вычисляем факториал числа 5, используя метод factorial.
print(f"Факториал: {factorial_of_5}")  # Выводим значение факториала.

# Демонстрация функций из number_transformer.py
squared_numbers = transform_with_map(numbers, lambda x: power(x, 2)) # Используем функцию transform_with_map для возведения каждого числа в списке numbers в квадрат (с помощью lambda-функции и power).
print(f"Числа в квадрате: {squared_numbers}") # Выводим список чисел, возведенных в квадрат.

even_numbers = filter_with_lambda(numbers, lambda x: x % 2 == 0) # Используем функцию filter_with_lambda для фильтрации списка numbers, оставляя только четные числа (с помощью lambda-функции).
print(f"Четные числа: {even_numbers}")  # Выводим список четных чисел.




