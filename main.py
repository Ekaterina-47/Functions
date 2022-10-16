from collections import Counter

# Функция 1:
def Func_1(n_customers):
    ID = []
    for i in range(0, n_customers):
        ID.append(i)
    # Создан массив ID из индексов со сквозной нумерацией, начинается с 0
    # Теперь для каждого эл из массива ID подсчитаю сумму цифр числа и определю эти суммы в массив Mass
    # Итоговым ответом будет колличество повторений каждого уникального элемента из массива Mass
    Mass = []
    for i in ID:
        summa = 0
        while i > 0:
            digit = i % 10
            summa = summa + digit
            i = i // 10
        Mass.append(summa)
    cnt = Counter(Mass)
    print(cnt)

# Функция 2
def Func_2 (n_customers, n_first_id):
    ID = []
    for i in range(n_first_id, n_customers):
        ID.append(i)
    # Аналогично Функции 1 создан массив ID, но теперь такой, который начинается с переданного в n_first_id значения
    # Далее идентичный алгоритм, что и в Функции 1. Считаем колличество повторений уникальных элементов в массиве
    Mass = []
    for i in ID:
        summa = 0
        while i > 0:
            digit = i % 10
            summa = summa + digit
            i = i // 10
        Mass.append(summa)
    cnt = Counter(Mass)
    print(cnt)