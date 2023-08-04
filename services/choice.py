from random import choice


def rps_choice():
    return choice(['Камень', 'Ножницы', 'Бумага'])


def get_winner(user: str, bot: str) -> str:
    rules: dict[str, str] = {'Камень': 'Ножницы',
                             'Ножницы': 'Бумага',
                             'Бумага': 'Камень'}

    if user == bot:
        return 'draw'
    elif rules[user] == bot:
        return 'win'
    else:
        return 'lose'
