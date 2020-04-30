# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : test3.py
# __time__  : 2020/4/24 2:23 PM

s = 'Ⅲ'
a = s.encode('utf-8')
print(a)

print(s.isnumeric())
print('III'.isnumeric())

'III Ⅲ'


class A:
    ''

class B:
    def __init__(self):
        self.name = [A(), A(), A()]

if __name__ == '__main__':
    b = B()

    b.name[0].__dict__ = {"name": 'mu'}
    b.name[1].__dict__ = {'Name': "n"}
    b.name[2].__dict__ = {'Nams': 's'}
    print(b.name[0].__dict__)
    print(b.name[1].__dict__)
    print(b.name[2].__dict__)
    print('')

