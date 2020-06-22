# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : test_01.py
# __time__  : 2020/6/22 3:32 下午

import easygui


if __name__ == "__main__":
    easygui.ynbox("Shall I continue?", "Title", ("Yes", "No"))
    easygui.msgbox("This is a basic message box.", "Title Goes Here")
    easygui.buttonbox(
        "Click on your favorite flavor.",
        "Favorite Flavor",
        ("Chocolate", "Vanilla", "Strawberry"),
    )
