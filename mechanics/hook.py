r'''псссст.... тебе тоже не нравится произвол механники core? я знаю как можно надуть его в два счёта!'''
if 'environment':
    from recursion import recursion
    from variables import variables
    from object import object as new_object
    import time

class hook():
    def __init__(self):
        pass


    def exec_input(self):
        #input('!!!before')
        command = recursion(variables.get('last_input'))
        #print(f'>>>"{command}"')
        #input('!!!after')
        if command.isdigit() or command in self.items():
            self.move(command)
        elif command.isspace() or command in ['']:
            pass
        else:
            i = 1
            items = self.items()
            while str(i) in items:
                i += 1
            self.this().set(str(i), command)


    def loop(self, *args):
        variables.set('loop', args)


    def this(self):
        return new_object(variables.get('point'))
    

    def items(self):
        return new_object(variables.get('point')).items()


    def point(self, point):
        variables.set('point', point)


    def move(self, item):
        variables.set('point', variables.get('point') + '.' + item)


    def back(self):
        variables.set('point', '.'.join(variables.get('point').split('.')[:-1]))


    def remove(self, object):
        if type(object).__name__: object.remove()
        else: return '???'

    
    def exit(self):
        exit()


hook = hook()