# -*- coding: utf-8 -*-
# __file__  : inter2.py
# __time__  : 2020/7/29 8:20 PM

class InterInt:

    def __init__(self):
        self.a = 1

    def __next__(self):
        a = yield self.a
        print(a)
        self.a += 1


# Expected results:
a = InterInt()
# print(next(a)) # 1
# print(next(a)) # 2
# print(next(a)) # 3

# class OddNum:
#     def __init__(self, target=100):
#         self.target = target
#
#     def __iter__(self):
#         value = 0
#         while value < self.target:
#             if value % 2 == 1:
#                 yield value
#             value += 1
#
# if __name__ == '__main__':
#     oddnum_gene = OddNum()
#
#     for value in oddnum_gene:
#         print(value)


class CustomDict:

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __missing__(self, key):
        if isinstance(key, str):

            raise KeyError(key)
        return self[str(key)]

    def __getitem__(self, item):
        return self.__dict__[item]
    # def __getitem__(self, item):

if __name__ == '__main__':
    cdict = CustomDict()

    cdict["a"] = 1

    cdict["b"] = 2
    print(cdict["a"])
    print(cdict["b"])
    print(cdict["c"])
