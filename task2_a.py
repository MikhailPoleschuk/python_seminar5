import random
n = int(input('На сколько конфет играете?-->'))
print(f'Условие задачи: На столе лежит {n} конфет.')
print('Играют два игрока делая ход друг после друга.')
print('Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.')
print('Все конфеты оппонента достаются сделавшему последний ход.')

ost = n

list_=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                  13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]


name1_ = 'любимый сын Саша' #input("Как тебя зовут -->")
name2_ = 'prosto BOT'
name1 = random.choice([name1_, name2_])

if name1 == name2_:
    bot_count = random.choice(list_)
    ost = ost - bot_count
    print(f'Бот взял {bot_count} конфет и осталось {ost}')
    name2 = name1_


while ost > 0:

    a = int(input(f'Сколько конфект возьмет игрок {name1_}? -->'))
    if 0 < a <= 28:
        ost = ost-a
        if ost == 0:
            print(f"игрок {name1_} забрал последние конфеты и Выйграл!!!")
            break
        print(f'осталось {ost} конфет')
        
        if ost<28:
            bot_count = ost # услажняем игру для Саши
            #list_=list_[0:ost]
        
        #bot_count = random.choice(list_) # услажняем игру для Саши и делаем бота чуть поумнее
        ost = ost - bot_count
        if ost == 0:
            print(f"prosto BOT забрал последние конфеты и Выйграл!!!")
            break
        print(f'Бот взял {bot_count} конфет и осталось {ost}')

    else:
        print('такое количество конфет брать нельзя')
