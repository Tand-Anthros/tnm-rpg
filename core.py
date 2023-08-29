r'''что? да я тоже механника, но я могу запсутить сама себя, как тебе такое?!'''
if 'environment':
    import sys, os
    sys.stderr = open('log.txt', 'w', encoding = 'utf-16')


def core():
    try:
        if 'change_system_path':
            if os.name == 'nt': slash = '\\'
            else: slash = '/'
            pos = slash.join(__file__.split(slash)[:-1])
            os.chdir('mechanics')
            sys.path[0] = pos + slash + 'mechanics'


        if 'importing_some_mechanics':
            from recursion import recursion
            from variables import variables


        if 'assignment_global_variables':
            variables.set('point', 'start')
            variables.set('loop', '$interface.clear, $interface.scene, $get, $hook.exec_input')
            variables.set('last_input', '')
        

        while 'main_loop':
            recursion(variables.get('loop'))

    except SystemExit:
        print('досвидания!')
    except:
        print('\n\nуууупс! кажется произошла ошибка, пожалуйста обратитесь за поддержкой в README.md')
        raise


core()