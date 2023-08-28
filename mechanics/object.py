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
        if not os.path.isfile(self.location): open(self.location, encoding = 'utf-16').write('{"":"???"}')

    
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
    

    def value(self):
        self.update()
        return self.content


    def get(self, item):
        self.update()
        if item in self.file.keys(): return True
        else: False


    def items(self):
        self.update()
        out = list()
        for key in self.file.keys():
            if key not in ['']: out.append(key)
        return out
    

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
            temp_file = temp_file[key]

        if item: temp_file[item] = {"":value}
        json.dump(self.file, open(self.location, 'w', encoding = 'utf-16'))