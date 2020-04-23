# -*- coding: utf-8 -*-
# __author__: MUSIBII
# __email__ : shaozuanzuan@gmail.com
# __file__  : test01.py
# __time__  : 2019-05-25 09:54

# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        print(1)
        new_num = yield average
        print(2)
        count += 1
        total += new_num
        average = total/count

# 委托生成器
def proxy_gen():
    while True:
        yield from average_gen()

# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)            # 预激下生成器
    print(calc_average.send(10))  # 打印：10.0
    # print(calc_average.send(20))  # 打印：15.0
    # print(calc_average.send(30))  # 打印：20.0

if __name__ == '__main__':
    main()