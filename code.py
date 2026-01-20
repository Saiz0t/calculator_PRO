def modify_result(k):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'Результат увеличенный на {k:.1f}: {result * k}, ' \
                   f'результат уменьшенный на {k:.1f}: {result / k}'
        return wrapper
    return decorator

@modify_result(2.1)
def add(a, b):
    return a + b

@modify_result(2.1)
def subtract(a, b):
    return a - b

@modify_result(2.1)
def multiply(a, b):
    return a * b

@modify_result(2.1)
def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Деление на ноль невозможно")

# Тестирование функций
print(add(3, 5))
print(subtract(10, 4))
print(multiply(7, 3))
print(divide(15, 3))