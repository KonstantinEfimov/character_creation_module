from math import sqrt

message = ('Добро пожаловать в самую лучшую программу'
           ' для вычисления квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Выводим результат вычислений корня."""
    if your_number <= 0:
        my_sguare = calculate_square_root(your_number)
        print(f'Мы вычислили квадратный корень из введённого вами числа.'
              f'Это будет: {my_sguare}')
        return


print(message)
calc(25.5)
