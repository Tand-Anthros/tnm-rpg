if 'environment':
    from object import object as new_object
    import os


def execution(mechanic, args = []):
    if 'create_mechanics_list':
        if os.name == 'nt': slash = '\\'
        else: slash = '/'
        pos = slash.join(__file__.split(slash)[:-1])

        mechanics = dict()
        for file in os.listdir():
            if os.path.isfile(pos + slash + file) and len(file) > 3 and file[-3:] == '.py': 
                mechanics[file[:-3]] = getattr(__import__(file[:-3]), file[:-3])


    attrs = mechanic.split('.')[1:]
    if mechanic[0] == '$':
        mechanic = mechanics[mechanic.split('.')[0][1:]]
        for attr in attrs: mechanic = getattr(mechanic, attr)
        out = mechanic(*args)
        if out in [None]: return ''
        else: return out

    elif mechanic[0] == '@':
        mechanic = new_object(mechanic.split('.')[0][1:])
        for attr in attrs: mechanic = getattr(mechanic, attr)
        return mechanic
    else:
        return '???'    