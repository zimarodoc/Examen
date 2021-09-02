def nomer(card):

    return '*' * len(card[:-4]) + card[-4:]



print(nomer(input('Введите номер карты')))