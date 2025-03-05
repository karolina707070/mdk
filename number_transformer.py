def power(number, exponent): #Определяем метод для возвеления числа в степень.
    """Возводит число в заданную степень."""
    return number ** exponent

def transform_with_map(numbers, transform_func): #Определяем метод для преобразования чисел применение map.
    """Применяет функцию transform_func к каждому числу в списке numbers."""
    return list(map(transform_func, numbers))

def filter_with_lambda(numbers, condition): #Определяем метод для фильтрация с использованием filter, lambda
    """Фильтрует список numbers, используя lambda-функцию condition."""
    return list(filter(condition, numbers))



