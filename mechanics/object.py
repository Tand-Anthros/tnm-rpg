r'''я объект, что? да objects это механника объектов, но ты смотришь на экземпляр и я объект!'''
from typing import Any


if 'environment':
    import json, os

class object():
    def __init__(self, point):
        if os.name == 'nt': slash = '\\'
        else: slash = '/'
        self.point = point.split('.')
        self.location = slash.join(__file__.split(slash)[:-2]) + slash + 'objects' + slash + self.point[0] + '.json'
        if not os.path.isfile(self.location): open(self.location, 'w', encoding = 'utf-16').write('{"":"???"}')

    
    def __str__(self):
        self.update()
        return self.content


    def __setitem__(self, item, value):
        self.update(item = item, value = value)


    def __getitem__(self, item):
        self.update()
        if item == '': return self.content
        return object('.'.join(self.point) + '.' + str(item))
    

    def __getattr__(self, item):
        self.update()
        if item == '': return self.content
        return object('.'.join(self.point) + '.' + str(item))
    

    def where(self):
        return self.point


    def value(self):
        self.update()
        return self.content


    def get(self, item):
        self.update()
        if item == '': return self.content
        return object('.'.join(self.point) + '.' + str(item))


    def set(self, item, value):
        self.update(item = item, value = value)


    def items(self):
        self.update()
        out = list()
        for key in self.child:
            if key not in ['']: out.append(key)
        return out
    

    def remove(self):
        beckup = self.update(item = 'removed', value = 'removed')
        removed = object('removed')
        max_iter = 0
        for item in removed.items():
            if str(item).isdigit():
                if int(str(item)) > max_iter:
                    max_iter = int(str(item))
        object('removed' + '.' + str(max_iter + 1)).set('.'.join(self.point), beckup[[*beckup.keys()][0]][''])


    def update(self, item = None, value = None):
        if not os.path.isfile(self.location):
            file = open(self.location, encoding = 'utf-16')
            file.write('{"":"???"}')
            file.close

        file = open(self.location, encoding = 'utf-16')
        self.file = json.load(file)
        file.close()
        if self.file.get(''): self.content = self.file['']
        else:
            self.file[''] = '???'
            self.content = '???'

        temp_file = self.file
        for key in self.point[1:]:
            if temp_file.get(key): 
                if type(temp_file[key]).__name__ != 'dict':
                    temp_file[key] = {"":temp_file[key]}
                if not temp_file[key].get(''): 
                    temp_file[key][''] = '???'
            else:
                temp_file[key] = {"":"???"}
            self.content = temp_file[key]['']
            remove_file = temp_file
            remove_key = key
            temp_file = temp_file[key]
        self.child = [*temp_file.keys()]

        if item == 'removed' and value == 'removed': 
            out = {remove_key: remove_file[remove_key]}
            del remove_file[remove_key]
            json.dump(self.file, open(self.location, 'w', encoding = 'utf-16'))
            return out
        elif item: temp_file[item] = {"":value}

        json.dump(self.file, open(self.location, 'w', encoding = 'utf-16'))