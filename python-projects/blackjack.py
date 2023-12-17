from random import choice

# Константа с картами и их значениями
CARDS = {'2' : 2, 
         '3' : 3, 
         '4' : 4, 
         '5' : 5, 
         '6' : 6, 
         '7' : 7, 
         '8' : 8, 
         '9' : 9, 
         '10': 10, 
         'J' : 10, 
         'Q' : 10, 
         'K' : 10, 
         'A' : 11}

# Функция выбора случайной карты из колоды
def pull_card(list_to_append):
    list_to_append.append(choice(list(CARDS.items())))
    return list_to_append

# Функция просмотра карт в руке
def show_your_hand(hand):
    res = ''
    for cards in hand:
        res += '| ' + str(cards[0]) + ' | '
    return res

# Основная функция, сравнивающая очки игрока и бота
def compare(player_hand, bot_hand):
    player_score = 0
    bot_score = 0
    for cards in player_hand:
        player_score += cards[1]
    for cards in bot_hand:
        bot_score += cards[1]
    #
    if player_score == bot_score:
        print('НИЧЬЯ!')
    elif player_score > 21 and bot_score < 21:
        print('Победил бот, в следущий раз точно повезёт!')
    elif player_score < 21 and bot_score > 21:
        print('Поздравляю, Вы победили!')
    elif player_score and bot_score <= 21:
        if bot_score < player_score:
            print('Поздравляю, Вы победили!')
        else:
            print('Победил бот, в следущий раз точно повезёт!')
    else:
        if bot_score > player_score:
            print('Поздравляю, Вы победили!')
        else:
            print('Победил бот, в следущий раз точно повезёт!')

    print('ИГРОК =', player_score)
    print('БОТ =', bot_score)

# "очень сложный ИИ", который не будет больше брать карты, если у него в руке 17 или больше очков
def ai_decide(bot_hand):
    score = 0
    for cards in bot_hand:
        score += cards[1]
    if score < 17:
        pull_card(bot_hand)
    else:
        pass
    return bot_hand

player_hand = []
bot_hand = []

game = True

print('Набери больше очков, чем у оппонента, но не более 21')
print('В одной руке может быть не более 5 карт')
print('Удачи!')
# Игра начинается с двумя картами в руке
pull_card(player_hand)
pull_card(player_hand)
pull_card(bot_hand)
pull_card(bot_hand)
print('Игра началась!')

while game:
    print('Твои карты: ')
    print(show_your_hand(player_hand))
    print('1 - Взять ещё')
    print('2 - Закончить игру')
    inp = input('>>> ')
    # Если игрок хочет взять карты:
    if inp == str(1):
        if len(player_hand) < 5:
            pull_card(player_hand)
        if len(player_hand) == 5:
            print('Больше карты брать нельзя!')
    # Если игрок хочет завершить игру:
    if inp == str(2):
    # логика бота: в руке не может быть больше 5 карт
    # на столе уже лежит 2 карты, значит можно взять ещё 3 карты
        count = 0
        while count < 3:
            ai_decide(bot_hand) 
            count += 1
        compare(player_hand, bot_hand)
        print('Карты игрока:')
        print(show_your_hand(player_hand))
        print('Карты бота:')
        print(show_your_hand(bot_hand))
        game = False

print('КОНЕЦ ИГРЫ!')
