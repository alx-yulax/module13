print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123


# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225

def reverse(number):
    reversed = 0
    while number > 0:
        last_digit = number % 10
        reversed = reversed * 10 + last_digit
        number //= 10
    return reversed


def main():
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))

    reversed_number_1 = reverse(number_1)
    reversed_number_2 = reverse(number_2)

    summ_numbers = reversed_number_1 + reversed_number_2

    reversed_summ_numbers = reverse(summ_numbers)
    print()
    print('Первое число наоборот:', reversed_number_1)
    print('Второе число наоборот:', reversed_number_2)
    print('Сумма:', summ_numbers)
    print()
    print('Сумма наоборот:', reversed_summ_numbers)


main()
