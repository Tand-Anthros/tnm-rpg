r'''я работаю с интерфейсом. все что ты выводишь на экран, появляется благодаря мне!'''
if 'environment':
    from object import object as new_object
    from recursion import recursion
    from variables import variables
    import os


class interface():
    def __init__(self):
        pass


    def clear(self):
        if os.name == 'nt': os.system('cls')
        else: os.system('clear')


    def scene(self):
        
        point_object = new_object(variables.get('point'))
        print(recursion(point_object.value()), end = '\n\n\n')
        for item in point_object.items():
            print(f'{item})', point_object[item])
        print()

    
interface = interface()