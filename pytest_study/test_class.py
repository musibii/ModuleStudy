# -*- coding: utf-8 -*-
# __file__  : test_class.py
# __time__  : 2020/7/3 5:30 PM

# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

    def three_test(self):
        assert 1 == 2

    def test_four(self):
        assert 2 == 3