r'''я считываю что пишут игроки и возвращаю результат. что ты говоришь? я не слышу! пиши громче!'''
if 'environment':
    from variables import variables

def get(line = '> '):
    variables.set('last_input', input(line))