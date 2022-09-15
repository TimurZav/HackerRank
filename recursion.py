# def CalcSumNumbers(A):
#     if not A:
#         return 0
#     else:
#         summ = CalcSumNumbers(A[1:])
#         summ = summ + A[0]
#         return summ
#
#
# L = [2, 3, 8, 11, 4, 6]
# summ = CalcSumNumbers(L)
# print("summ = ", summ)


# # Рекурсивная функция - возвращает сумму чисел, обрабатывает вложенные списки
# def CalcSumNumbers(A):
#     summ = 0
#     # здесь нужно реализовать обход в цикле
#     for t in A:
#         # Обрабатывается элемент t
#         if not isinstance(t, list):  # проверить, есть ли t списком
#             summ = summ + t  # если t - не список, то прибавить его к сумме
#         else:
#             # получить сумму из следующих рекурсивных вызовов
#             summ = summ + CalcSumNumbers(t)
#
#     return summ
#
#
# # Демонстрация использования функции CalcSumNumbers()
# # 1. Создать набор чисел
#
# L = [-2, 3, 8, 11, [-4, 6, [2, [-5, 4]]]]
#
# # 2. Вызвать функцию
# summ = CalcSumNumbers(L)
#
# # 3. Распечатать сумму
# print("summ = ", summ)


# # Рекурсия. Реверсирование числа
# import math
#
#
# # Рекурсивная Функция
# def ReverseNumber(num):
#     # 1. Проверка, корректно ли число
#     if num < 0:
#         return -1
#
#     # 2. Проверка, равно ли число 0
#     if num == 0:
#         return 0
#
#     # 3. Если число корректно (num>0), то обработать его
#     # 3.1. Определить порядок числа (количество цифр в числе)
#     n_digit = 0  # порядок числа
#     num2 = num  # копия num
#
#     while num2 > 0:
#         n_digit = n_digit + 1
#         num2 = num2 // 10
#
#     # 3.2. Взять последнюю цифру из числа
#     t = num % 10  # 123456 => 6
#
#     # 3.3. Умножить последнюю цифру на 10^n_digit
#     res = t * int(math.pow(10, n_digit - 1))
#
#     # 3.4. Вернуть сумму с вызовом рекурсивной функции
#     return res + ReverseNumber(num // 10)
#
#
# # Демонстрация использования функции
# num = 1234000567
# rnum = ReverseNumber(num)  # rnum =   7650004321
# print("rnum = ", rnum)


# def GetMaxList(L):
#     if len(L) > 1:
#         # Получить максимум из следующих рекурсивных вызовов
#         Max = GetMaxList(L[1:])
#         # Сравнить максимум с первым элементом списка
#         if L[0] < Max:
#             return Max
#         else:
#             return L[0]
#
#     if len(L) == 1:  # последний элемент в списке
#         return L[0]  # вернуть этот элемент
#
#
# # Демонстрация использования функции Power()
# L = [ 500, 2300, 800, 114, 36]
# res = GetMaxList(L)
# print("res = ", res)

import math


def Convert_10_to_2_R(n, k):
    if n > 0:
        t = n % 2
        return int(t*math.pow(10, k)) + Convert_10_to_2_R(n//2, k+1)
    else:
        return 0


res1 = Convert_10_to_2_R(126, 0)  # Вызов рекурсивной функции
print("res1 = ", res1)

