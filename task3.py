# Создайте программу для игры в ""Крестики-нолики"".
import random
def win(pole_, str_):

    if pole_[0][0] == str_ and pole_[0][1] == str_ and pole_[0][2] == str_:

        win = 1
    elif pole_[1][0] == str_ and pole_[1][1] == str_ and pole_[1][2] == str_:

        win = 1
    elif pole_[2][0] == str_ and pole_[2][1] == str_ and pole_[2][2] == str_:

        win = 1
    elif pole_[0][0] == str_ and pole_[1][0] == str_ and pole_[2][0] == str_:

        win = 1
    elif pole_[0][1] == str_ and pole_[1][1] == str_ and pole_[2][1] == str_:

        win = 1
    elif pole_[0][2] == str_ and pole_[1][2] == str_ and pole_[2][2] == str_:

        win = 1
    elif pole_[0][0] == str_ and pole_[1][1] == str_ and pole_[2][2] == str_:

        win = 1
    elif pole_[0][2] == str_ and pole_[1][1] == str_ and pole_[2][0] == str_:

        win = 1
    else:
        win = 0
    return win


pole_ = [['?', '?', '?'],
         ['?', '?', '?'],
         ['?', '?', '?']]
for i in range(3):
    print(*pole_[i], '\n')

end_ = 0


while end_ < 10:
    # ставим X
    x_ok=0
    while x_ok < 1:
        x = input(f'куда поставим Х через запятую (столбик, строка)-->')
        list = x.split(',')
        line = int(list[0])-1
        column = int(list[1])-1

        if pole_[column][line] == 'X':
            print('Поле занято')
        elif pole_[column][line] == 'O':
            print('Поле занято')   
        else:
            pole_[column][line] = 'X'
            x_ok = 1
            end_+=1
    # Выйгрыши
    if win(pole_, 'X') == 1:
        print("Крестики победили!")
        for i in range(3):
            print(*pole_[i], '\n')
        break
        
    # ставим O
    o_ok=0
    while o_ok < 1:
        bot_line = random.choice([0, 1, 2])
        bot_column = random.choice([0, 1, 2])
        if pole_[bot_column][bot_line] == '?':
            pole_[bot_column][bot_line] = 'O'
            o_ok = 1
            end_+=1
    # ****************

    if win(pole_, 'O') == 1:
        print("Нолики победили :(")
        for i in range(3):
            print(*pole_[i], '\n')
        break
    
    for i in range(3):
        print(*pole_[i], '\n')    
            
