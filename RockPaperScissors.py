from random import randint

player = input('камень(к), ножницы(н) или бумага(б) ')

while player not in ('к', 'н', 'б'):
    print('Ошибка, давай попробуем еще раз')
    player = input('камень(к), ножницы(н) или бумага(б) ')

print(player, 'против', end=' ')

chosen = randint(1,3)

if chosen == 1:
    chosen = "к"
elif chosen == 2:
    chosen = 'н'
else:
    chosen = 'б'
print(chosen)

if player == chosen:
    print('Ничья!')
elif (player == 'к' and chosen == 'н') or (player == 'н' and chosen == 'б') or (player == 'б' and chosen == 'к'):
    print('Победил игрок')
else:
    print('Победил компьютер')