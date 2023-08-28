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
        print(recursion(variables.get('last_input')))
        time.sleep(3)


    def loop(self, *args):
        variables.set('loop', args)


    def this(self):
        return new_object(variables.get('point'))
    

    def items(self):
        return new_object(variables.get('point')).items()


    def point(self, point):
        variables.set('point', point)


    def choice(self, item):
        variables.set('point', variables.get('point') + '.' + item)


hook = hook()