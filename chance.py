basket = list(map(int, input('Введите через пробелы различные числа: ').split()))
x = int(input('Введите число, шанс которого вы хотите узнать: '))
if x in basket:
    my_dict = {i:basket.count(i) for i in basket}
    lenght = len(basket)
    y = my_dict.get(x)
    print('Шанс выпадение ' + str(x) + ' равна ' + str(round((y * 100) / lenght)) + '%')
elif x not in basket:
    print('Цифры' + str(x) + 'нет внутри корзины')
