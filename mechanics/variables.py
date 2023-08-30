if 'environment':
    import json, os


if 'zeroing_temp.json':
    if os.name == 'nt' and not os.path.isfile('__pycache__\\temp.json'): json.dump(dict(), open('__pycache__\\temp.json', 'w', encoding = 'utf-16'))
    elif not os.path.isfile('__pycache__/temp.json'): out = json.dump(dict(), open('__pycache__/temp.json', 'w', encoding = 'utf-16'))


class variables():
    def __init__(self):
        pass


    def get(self, item):
        if os.name == 'nt': out = json.load(open('__pycache__\\temp.json', encoding = 'utf-16'))
        else: out = json.load(open('__pycache__/temp.json', encoding = 'utf-16'))
        if item: return out.get(item)
        else: return out
    

    def set(self, item, value):
        file = self.get(None)
        file[item] = value
        if os.name == 'nt': json.dump(file, open('__pycache__\\temp.json', 'w', encoding = 'utf-16'))
        else: out = json.dump(file, open('__pycache__/temp.json', 'w', encoding = 'utf-16'))


variables = variables()