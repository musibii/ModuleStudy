# -*- coding: utf-8 -*-
# __file__  : website.py
# __time__  : 2020/7/4 6:16 PM

from xml.sax.handler import ContentHandler
from xml.sax import parse
import os


class Dispatcher:
    def dispatch(self, prefix, name, attrs=None):  # 定义调用某一具体方法的函数
        mname = prefix + name.capitalize()  # prefix（前缀）连接首字母大写的name
        dname = 'default' + prefix.capitalize()  # default连接首字母大写的prefix
        method = getattr(self, mname, None)  # 通过mname方法获取方法对象
        if callable(method):
            args = ()  # 如果method可调用，创建空的参数元组
        else:  # 如果method不可调用
            method = getattr(self, dname, None)  # 使用getattr获取dname的处理程序
            args = name,  # 将args设置为只包含标签名的元组
        if prefix == 'start': args += attrs,  # 如果调用的是起始程序，将属性添加到参数元组args中
        if callable(method): method(*args)  # 如果method可调用，传入参数调用方法

    def startElement(self, name, attrs):  # 重写开始元素的方法
        self.dispatch('start', name, attrs)  # 调用某一具体方法

    def endElement(self, name):  # 重写结束元素方法
        self.dispatch('end', name)  # 调用某一具体方法


class WebsiteConstructor(Dispatcher, ContentHandler):  #
    passthrough = False  # 开关变量

    def __init__(self, directory):
        self.directory = [directory]  # 创建目录列表
        self.ensureDirectory()  # 创建根目录

    def ensureDirectory(self):  # 定义创建目录的方法
        path = os.path.join(*self.directory)  # 定义路径
        os.makedirs(path, exist_ok=True)  # 创建目录，exist_ok=True表明如果创建目录已存在，不会抛出错误

    def startDirectory(self, attrs):  # 定义读取到目录开始标记的方法
        self.directory.append(attrs['name'])  # 添加目录名称到目录列表
        self.ensureDirectory()  # 创建目录

    def endDirectory(self):  # 定义到读取目录结束标记的方法
        self.directory.pop()  # 弹出目录

    def writeHeader(self, title):  # 定义写入头部HTML代码的方法
        self.out.write('<html>\n <head>\n <title>')
        self.out.write(title)
        self.out.write('</title>\n </head>\n <body>\n')

    def writeFooter(self):  # 定义写入尾部HTML的方法
        self.out.write('\n </body>\n</html>\n')

    def startPage(self, attrs):  # 定义读取到页面开始标记的方法
        filename = os.path.join(*self.directory + [attrs['name'] + '.html'])  # 创建页面路径
        self.passthrough = True  # 打开开关，写入页面内容
        self.out = open(filename, 'w')  # 创建HTML页面文件
        self.writeHeader(attrs['title'])  # 写入页面头部HTML代码

    def endPage(self):  # 定义读取到页面结束标记的方法
        self.passthrough = False  # 关闭开关
        self.writeFooter()  # 写入页面尾部的HTML代码
        self.out.close()  # 关闭创建的HTML文件

    def defaultStart(self, name, attrs):  # 定义读取到开始标记的默认方法
        if self.passthrough:  # 如果开关打开
            self.out.write('<' + name)
            if not attrs.items():
                self.out.write('>')
            # 写入开始标记
            for key, val in attrs.items():  # 循环读取属性的键值
                self.out.write(' {}="{}"'.format(key, val))  # 写入开始标记的属性
                self.out.write('>')  # 写入开始标记结束符

    def defaultEnd(self, name):  # 定义读取到结束标记的默认方法
        if self.passthrough:  # 如果开关打开
            self.out.write('</{}>'.format(name))  # 写入结束标记

    def characters(self, chars):  # 定义读取到标记内容的方法
        if self.passthrough:  # 如果开关打开
            self.out.write(chars)  # 写入内容


if __name__ == '__main__':
    parse('website.xml', WebsiteConstructor('public_html'))
