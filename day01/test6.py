# -*- coding: utf-8 -*-
# __file__  : test6.py
# __time__  : 2020/6/24 9:33 下午

import unittest, my_math2
from subprocess import Popen, PIPE

import pylint


class ProductTestCase(unittest.TestCase):
    def test_with_PyLint(self):
        cmd = "pylint", "-rn", "my_math2"  # -rn  关闭报告，只显示警告和错误
        pylints = Popen(cmd, stdout=PIPE, stderr=PIPE)
        print(pylints.stdout.read())
        print("*" * 50)
        self.assertEqual(pylints.stdout.read().decode(), "")


if __name__ == "__main__":
    unittest.main()
