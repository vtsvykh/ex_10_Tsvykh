def convert_roma_arab():
    roma = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    list = []
    j = 0
    replay = 0
    summa = 0
    # создание списка с разбиением символов и их вознесения в верхний регистр
    number = input("Введите римское число [от I до MMMCMXCIX]: ")
    list += number.upper()
    # перевод элементов списка в числа
    try:
        list = [roma[x] for x in list]
    except KeyError:
        print("Недопустим-ый/-е символ/-ы. Допустимые символы M, D, C, L, X, V, I!")
        return convert_roma_arab()
    # конвертирование в одно число
    while j <= len(list)-1:
        try:
            # проверка повторения одного символа подряд
            if replay > 2:
                print("Число повторов одного символа превышает допустимое значение!")
                return convert_roma_arab()
    # проверка елементов из списка и присвоение им нужной роли
            # M, C, X, I
            if list[j] == 1 or list[j] == 10 or list[j] == 100 or list[j] == 1000:
                # проверка на вычитание числа
                if list[j+1] == list[j] * 5 or list[j+1] == list[j] * 10:
                    # проверка на повторении меньшей цифры слева от большой
                    if replay > 0:
                        print("Повторения меньшей цифры не допускаются перед большей!")
                        return convert_roma_arab()
                    summa -= list[j]
                # проверка на правильную последовательность римских чисел
                elif list[j+1] > list[j] * 10:
                    print("Ошибка последовательности символом. IV, IX, XL, XC, CD, CM")
                    return convert_roma_arab()
                # иначе происходит сложение числа
                else:
                    summa += list[j]
                # счетчик повтора символов I, X, C, M
                if list[j] == list[j+1]:
                    replay += 1
                else:
                    replay = 0
            # D, L, V
            else:
                # проверка на правильную последовательность римских чисел
                if list[j] < list[j+1]:
                    print("Ошибка последовательности символом. M -> D -> C -> L -> X -> V -> I")
                    return convert_roma_arab()
                # проверка на повторимость чисел
                elif list[j] == list[j+1]:
                    print("Число повторов одного символа превышает допустимое значение!")
                    return convert_roma_arab()
                else:
                    summa += list[j]
        except IndexError:
            summa += list[j]
        finally:
            j += 1
    # вывод результата
    print("Арабское число: " + str(summa))

v = 4
print(v.convert_roma_arab())

